from data import *
from classesandmethods import *

def main() -> int:
    # GUI DEBUG #
    try:
        RUN("python -m gui.pressCheck", check=True)
    except Exception as e:
        print(e)
    
    # # DOCUMENT CLASS DEBUG #
    # DOC(input("Enter document type: "), input("Enter name of document: "))

    return 0

if __name__ == "__main__":
    main()