import pypdf
from pathlib import Path

def run(book):
    book = Path(book)

    if book.exists():
        read = pypdf.PdfReader(book)
        md = read.metadata
    else:
        print("Hmm, this file does not exist.")

def fields(book):
    book = Path(book)

    if book.exists():
        read = pypdf.PdfReader(book)
        md = read.metadata
    else:
        print("Hmm, this file does not exist.")
        return

    print(f"Values of file {book}")
    for key, val in md.items():
        print(f"{key}: {val}")

def title(book):
    book = Path(book)
    
    if book.exists():
        read = pypdf.PdfReader(book)
        md = read.metadata
    else:
        print("Hmm, this file does not exist.")
        return

    if md.title:
        return md.title
    if md.get("/Subject"):
            return md.get("/Subject")
    
