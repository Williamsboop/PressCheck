from data import *
from ..methods import *

class DOC:
    def __init__(self, path: str, type: str) -> None:
        self.__path: str = path
        self.__name: str = BASE_FILE(path) # Ex. 'Publication_9_18_25.pdf' 
        self.__type: str = type # Newspaper, Runsheet, Supplement, Etc.
        self.__pdf: PDF = PDF(self.__path)
        self.__html_blocks: dict = {} # Holds each page as html.
        self.__imgs: dict = {} # Holds each page as an image.

        match self.__type.lower():
            case "runsheet":
                self.__html_blocks = TO_HTML(self.__name, self.__pdf)
            case "newspaper" | "supplemental":
                self.__html_blocks = TO_HTML(self.__name, self.__pdf)
                self.__imgs = TO_IMGS(self.__name, self.__pdf)
            case _:
                LOG.debug(f"Error: {self.__type} is not a valid document type.")
    
    @property
    def path(self) -> str:
        return self.__path
    
    @property
    def name(self) -> str:
        return self.__name
                
    @property
    def type(self) -> str:
        return self.__type
                
    @property
    def pdf(self) -> PDF:
        return self.__pdf
                
    @property
    def html_blocks(self) -> dict:
        return self.__html_blocks
    
    @property
    def imgs(self) -> dict:
        return self.__imgs