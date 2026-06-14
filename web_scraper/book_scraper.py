import csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup

# 1. TARGET WEBSITE
URL = "http://books.toscrape.com/"

def scrape_books():
    print(f"Connecting to {URL}...")
    
    # Send a request to open the webpage
    response = requests.get(URL)
    
    # Check if the website responded successfully (Status Code 200)
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 2. FIND ALL BOOK ARTICLES ON THE PAGE
    # On this site, every book is contained inside an <article class="product_pod"> tag
    book_elements = soup.find_all("article", class_="product_pod")
    
    scraped_data = []
    
    print(f"Found {len(book_elements)} books. Extracting details...")

    # 3. LOOP THROUGH EACH BOOK AND EXTRACT DATA
    for book in book_elements:
        # Extract Title (found inside the <h3> <a> tag's 'title' attribute)
        title = book.h3.a["title"]
        
        # Extract Price (found inside a <p> tag with class 'price_color')
        price = book.find("p", class_="price_color").text
        
        # Extract Availability (found inside a <p> tag with class 'instock availability')
        availability = book.find("p", class_="instock availability").text.strip()
        
        # Clean up the price string (removing the weird currency symbol if needed)
        clean_price = price.replace("£", "$") # Swapping to dollars for ease
        
        # Append to our data list as a dictionary
        scraped_data.append({
            "Title": title,
            "Price": clean_price,
            "Status": availability
        })

    # 4. EXPORT TO A CSV FILE
    # This will save right in the folder where you run the script
    output_file = Path(r"C:\Users\PMLS\Desktop\tracked_books.csv")
    
    # Define the headers for our spreadsheet
    headers = ["Title", "Price", "Status"]
    
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Write the top row
        writer.writerows(scraped_data)  # Write all the book rows

    print(f"\n🎉 Success! Data saved to: {output_file.resolve()}")

if __name__ == "__main__":
    scrape_books()
