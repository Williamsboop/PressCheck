from logging import basicConfig, DEBUG, getLogger
from typing import Any
import customtkinter as gui
from screeninfo import get_monitors, Monitor
import ctypes
from json import load
from subprocess import run as RUN
from pytesseract import image_to_string, pytesseract, TesseractNotFoundError
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
from os import path
from fitz import open
from bs4 import BeautifulSoup
from bs4.element import Tag

CTk = gui.CTk
LANCZOS = getattr(Image, "LANCZOS")
IMAGE = Image
ENHANCE = ImageEnhance
FILTER = ImageFilter
DRAW = ImageDraw
PATH = path
BASE_FILE = path.basename
basicConfig(level=DEBUG)
LOG = getLogger(f" {__name__} ")
PDF = open
HTML_  = BeautifulSoup
HTML_TAG = Tag

def disable_parsing_logs() -> None:
    getLogger('PIL').setLevel('ERROR')
    getLogger('pytesseract').setLevel('ERROR')

def TES_ENG_SETTR(path: str) -> None:
    pytesseract.tesseract_cmd = path

__all__ = ['LOG',
           'Any',
           'gui', 
           'CTk', 
           'get_monitors', 
           'Monitor', 
           'ctypes', 
           'load', 
           'RUN',
           'image_to_string',
           'TesseractNotFoundError',
           'LANCZOS',
           'IMAGE',
           'ENHANCE',
           'FILTER',
           'TES_ENG_SETTR',
           'disable_parsing_logs',
           'PATH',
           'BASE_FILE',
           'PDF',
           'HTML_',
           'HTML_TAG',
]