from data import *
from lib import *

def main() -> int:
    disable_parsing_logs()
    
    
    # # GUI DEBUG #
    # try:
    #     RUN("python -m gui.engine", check=True)
    # except Exception as e:
    #     print(e)
    
    
    # # DOCUMENT CLASS DEBUG #
    # DOC(input("Enter document type: "), input("Enter name of document: "))


    # # GETTING TEXT FROM IMAGES TESTING #
    # print("\n\n[ NOT ENHANCED ]\n\n")
    # full_res_text = READ_IMG("dev\\OCR Testing Images\\full_res.png")
    # print(f"\nFull Resolution:\n\n{full_res_text}\n")
    
    # ad_text = READ_IMG("dev\\OCR Testing Images\\ad_A.png")
    # print(f"\nAd-A:\n\n{ad_text}\n")
    
    
    # # IMG CLASS DEBUG #
    # try:
    #     myImg = IMG(IMAGE.open(input("Enter path to image: ")))
    #     print(myImg)
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    
    
    # DOC CLASS DEBUG #
    myDoc = DOC("dev\\pdfs\\runsheet.pdf", "Runsheet")

























    
    
    
    
    
    
    #- CODE EXIT -#
    return 0
    #- CODE EXIT -#


if __name__ == "__main__":
    main()