from data import *
from ..methods import READ_IMG

class IMG:
    
    def __init__(self, img: IMAGE.Image) -> None:
        self.__img = img
        self.__path = getattr(img, 'filename', 'Unnamed Image')
        self.__name = BASE_FILE(getattr(img, 'filename', 'Unnamed Image'))
        self.__dpi = self.__img.info['dpi'][0] if 'dpi' in self.__img.info else "Unavailable"
        self.__width, self.__height = self.__img.size
        self.__text = READ_IMG(self.__path)
                
    def __str__(self) -> str:
        return f"""
Path: {self.__path}
Filename: {self.__name}
Size: {f"width: {self.__width}px | height: {self.__height}px"}
DPI: {self.__dpi}
Text: {self.__text}
        """