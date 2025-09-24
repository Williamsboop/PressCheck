from data import *

class IMG:
    
    def __init__(self, img: IMAGE.Image) -> None:
        self.__img = img
        self.__name = BASE_FILE(getattr(img, 'filename', 'Unnamed Image'))
        self.__dpi = self.__img.info['dpi'][0]
                
    def __str__(self) -> str:
        return f"""
    Name: {self.__name}
    Size: {self.__img.size}
    DPI: {self.__dpi}            
"""