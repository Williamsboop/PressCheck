from data import *
from ..methods.FORMAT import TO_HTML, TO_IMGS

@dataclass
class DOC:
    type: str # Newspaper, Runsheet, Supplement, Etc.
    name: str # Ex. 'DEE_9_18_25.pdf'
    pages_as_html: dict = field(init=False) # Holds each page as html.
    pages_as_imgs: dict = field(init=False) # Holds each page as an image.

    def __post_init__(self) -> None:
        self.type = self.type.lower()
        self.name = f"{self.name.upper()}.pdf"
        match self.type:
            case "runsheet":
                self.pages_as_html = TO_HTML(self.name)
            case "newspaper":
                self.pages_as_html = TO_HTML(self.name)
                self.pages_as_imgs = TO_IMGS(self.name)
            case "supplement":
                self.pages_as_imgs = TO_IMGS(self.name)
            case _:
                LOG.debug(f"Error: {self.type} is not a valid document type.")