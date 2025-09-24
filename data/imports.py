from logging import basicConfig, DEBUG, getLogger
from typing import Any
import customtkinter as gui
CTk = gui.CTk
from screeninfo import get_monitors, Monitor
import ctypes
from json import load
from subprocess import run as RUN
from dataclasses import dataclass, field
basicConfig(level=DEBUG)
LOG = getLogger(f" {__name__} ")
from pytesseract import image_to_string, pytesseract, TesseractNotFoundError
from PIL import Image, ImageEnhance, ImageFilter
LANCZOS = getattr(Image, "LANCZOS")
IMAGE = Image
ENHANCE = ImageEnhance
FILTER = ImageFilter

def disable_parsing_logs() -> None:
    getLogger('PIL.PngImagePlugin').disabled = True
    getLogger('pytesseract').disabled = True

def TES_ENG_SETTR(path: str) -> None:
    pytesseract.tesseract_cmd = path

__all__ = ['LOG',
           'dataclass',
           'field',
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
]