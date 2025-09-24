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
from easyocr import Reader as GET_TEXT

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
            'GET_TEXT',
]