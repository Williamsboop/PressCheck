from data import *

HERE = PATH.dirname(__file__)
ICO_LOGO: str = PATH.join(HERE, "Logo.ico")
PNG_LOGO: str = PATH.join(HERE, "Logo.png")
VERSION_INFO: str = PATH.join(HERE, "version_info.json")

__all__ = [
    "ICO_LOGO",
    "PNG_LOGO",
    "VERSION_INFO",
]