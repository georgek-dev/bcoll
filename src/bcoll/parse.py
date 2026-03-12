import ebooklib
import pypdf
from pathlib import Path

book = Path(r"D:\Downloads\CHIP_01_2024_B.pdf")

if book.exists():
    read = pypdf.PdfReader(book)
    md = read.metadata
else:
    print("Hmm, this file does not exist.")

def fields():
    global md, book

    print(f"Values of file {book}")
    for key, val in md.items():
        print(f"{key}: {val}")

def title():
    global md

    if md.title:
        return md.title

    if md.get("/Subject"):
        return md.get("/Subject")

fields()
print("Book: " + title() + " by " + md.author)
