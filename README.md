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
|   main.py
|
+---assets
|       version_info.json
|
+---classes
|       DOC.py
|       FORMAT.py
|       __init__.py
|
+---data
|       imports.py
|       __init__.py
|
\---gui
        pressCheck.py
        __init__.py
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
- **assets/**: Contains icons and version information.
- **classes/**: Python modules for document and format logic.
- **data/**: Data utilities and import scripts.
- **documents/**: Place your documents here. Use `checked/` and `unchecked/` for organization.
- **gui/**: GUI code for the application.


## Future Plans

- **User-Configurable Parsing:** Users will be able to designate parsing details for specific PDFs via user-configurable JSON files, allowing for flexible and tailored document processing.
- **Upload to Repositories:** Users will be able to upload completed files to designated repositories, including both local and cloud storage. Initial cloud support will focus on Google Drive, with the possibility of adding more services in the future.
- **Webscraping for PDF Downloads:** Users will be able to specify websites or servers from which PDFs can be downloaded directly through the application's webscraping capabilities.
- **SmartPublisher API Support:** If available, SmartPublisher API integration would allow for automatic Runsheet acquisition, streamlining the document collection process.

## Author

Williamsboop ( Cameron Williams )