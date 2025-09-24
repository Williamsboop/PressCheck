from data import *

def parse_img(path: str) -> str:
    TES_ENG_SETTR('tesseract_engine\\tesseract.exe')
    try:
        return image_to_string(path)
    except TesseractNotFoundError:
        return "Tesseract executable not found. Please ensure it's installed and the path is correct."
    except Exception as e:
        return f"An error occurred: {e}"