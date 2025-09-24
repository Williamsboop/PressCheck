# Get project imports.
from data import *

# HTML dict will be formatte as such: 'pdfname_i(nth)' : [page_num, html_code, extracted_text]
def TO_HTML(file: str) -> dict:
    LOG.debug(f"TO_HTML: {file}")
    tempDict = {}
    return tempDict

# Img dict will be formatte as such: 'img_name' : [page_num, img_size, extracted_text]
def TO_IMGS(file: str) -> dict:
    LOG.debug(f"TO_IMGS: {file}")
    tempDict = {}
    return tempDict