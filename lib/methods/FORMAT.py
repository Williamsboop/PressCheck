# Get project imports.
from data import *

# HTML dict will be formatte as such: 'pdfname_i(nth)' : [page_num, html_code, extracted_text]
def TO_HTML(name: str, pdf: PDF) -> dict:
    html: str = ""
    
    try:
        for page in pdf.pages():
            html += page.get_text("html")
        
        _html_ = HTML_(html, "lxml")
        
        for tag in _html_.find_all(True):
            if isinstance(tag, HTML_TAG):
                format_styles(tag)
        
        # parsable_html = flatten_html(parsable_html)
        
        DEBUG_createHTML(name, str(_html_.prettify()))
    
    except Exception as e:
        print(e)
    
    return {}

def format_styles(tag: HTML_TAG):
    
    if 'style' not in tag.attrs:
        return
    
    styles = str(tag['style']).split(';')
    new_styles = []
    
    for style in styles:
        style = style.strip()
        if not style:
            continue
        if ':' not in style:
            continue
        key, value = style.split(":", 1)
        if key.strip().lower() == "font-size":
            new_styles.append(f"{key.strip()} : {value.strip()}")

    if new_styles:
        tag["style"] = "; ".join(new_styles)
    else:
        del tag.attrs['style']

# Img dict will be formatte as such: 'img_name' : [page_num, img_size, extracted_text]
def TO_IMGS(name: str, pdf: PDF) -> dict:
    return {}

def DEBUG_createHTML(name: str, html: str) -> None:
    
    LOG.debug(f"Creating HTML for {name.rsplit('.', 1)[0]}.html ...")
    
    out_path = "dev\\html"
    with open(out_path + f"\\{name.rsplit('.', 1)[0]}.html", "w", encoding="utf-8") as file:
        file.write(html)