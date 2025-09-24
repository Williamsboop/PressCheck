<p align="center">
   <img src="assets/Logo.png" alt="PressCheck Logo" width="120"/>
</p>

# PressCheck

PressCheck is a Python application designed to help you manage and verify documents efficiently. It features a graphical user interface (GUI) for easy interaction, document organization, and format checking.

## Features
- Document verification and management
- Organized storage for checked and unchecked documents
- GUI for user-friendly operation
- Customizable document formats

## Project Structure
```
PressCheck
|   .gitignore
|   LICENSE
|   main.py
|   README.md
|
+---assets
|   |   Logo.ico
|   |   Logo.png
|   |   version_info.json
|
+---classesandmethods
|   |   DOC.py
|   |   FORMAT.py
|   |   PARSER.py
|   |   __init__.py
|   
| 
+---data
|   |   imports.py
|   |   __init__.py
|
+---gui
|   |   engine.py
|   |   __init__.py
|
\---tesseract_engine
```

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Required packages (see below)

### Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/Williamsboop/PressCheck.git
   cd PressCheck
   ```
2. (Optional) Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

### Running the Application
Run the main script:
```powershell
python main.py
```


## Folder Descriptions
- **assets/**: Icons, logo, and version information.
- **classesandmethods/**: Core document, format, and parser logic (DOC, FORMAT, PARSER).
- **data/**: Data utilities and import scripts.
- **gui/**: GUI engine and related code.
- **tesseract_engine/**: (Purpose not described—add details if needed.)
- **.vscode/**: VS Code workspace settings.
- **.gitignore, LICENSE, README.md, main.py**: Project config, license, docs, and entry point.



## TODO / Ideas

- [ ] User-configurable parsing for PDFs (via JSON files)
- [ ] Upload completed files to repositories (local & cloud, e.g., Google Drive)
- [ ] Webscraping for PDF downloads from user-specified sources
- [ ] SmartPublisher API integration for automatic Runsheet acquisition
- [ ] Add user authentication and permissions
- [ ] Batch processing of documents
- [ ] Enhanced error handling and logging
- [ ] Export reports in multiple formats (PDF, CSV, etc.)
- [ ] Improved UI/UX and theming options

## pytesseract


This project uses [pytesseract](https://github.com/madmaze/pytesseract) as a Python wrapper for Google's Tesseract-OCR Engine. You must have the Tesseract executable installed and available in your system PATH or specify its location in your code. For more information, see the [pytesseract documentation](https://pypi.org/project/pytesseract/).

**Note:** The Tesseract-OCR Engine will be included in future releases of PressCheck for easier setup and use.

### pytesseract License

```
Copyright (c) 2014 Samuel Hoffstaetter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Author

Williamsboop ( Cameron Williams )