# file-organizer-python
A Python script that automatically sorts files into categorized folders based on their extensions.
# Automated File Organizer

A Python automation script that cleans up cluttered directories (like your Downloads or Desktop) by instantly sorting files into organized folders based on their extensions.

## Features
* Automatically detects file types (Images, Documents, Spreadsheets, Installers, Zips).
* Safely creates destination directories only if matching files exist.
* Uses Python's built-in `pathlib` and `shutil` libraries for robust file handling across operating systems.

## Built With
* **Python 3**
* `pathlib` (For object-oriented file paths)
* `shutil` (For high-level file operations/moving)

## How It Works
The script maps extensions to their respective target folders. For example:
* `.png`, `.jpg` `/Images`
* `.pdf`, `.docx`, `.txt` `/Readings_and_Docs`

## Setup and Usage
1. Clone this repository or download the `test.py` script.
2. Open the script and modify the `WATCH_DIRECTORY` variable to point to the folder you want to clean up:

```python
WATCH_DIRECTORY = Path(r"C:\Your\True\Path\Here")
```

## Demo Video
[[video]] https://github.com/Nancyautomation/file-organizer-python/raw/main/file-organizer-demo.mp4





