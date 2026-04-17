from pathlib import Path

from ebooklib import epub
from rich import print


def eprun(book):
    book = Path(book)

    if book.exists():
        read = epub.read_epub(book)
        # return read
    else:
        print("Hmm, this file does not exist.")


def epfields(book):
    book = Path(book)

    if book.exists():
        read = epub.read_epub(book)
        md = read.metadata
    else:
        print("Hmm, this file does not exist.")
        return

    fields = [
        "identifier",
        "title",
        "language",
        "creator",
        "contributor",
        "publisher",
        "rights",
        "coverage",
        "date",
        "description",
    ]
    print(f"Values of file [bold cyan]{book}[/bold cyan]")
    for item in fields:
        field = read.get_metadata("DC", item)
        print(f"[bold green]DC:{item}[/bold green] [blue]{field}[/blue]")


def eptitle(book):
    book = Path(book)

    if book.exists():
        read = epub.read_epub(book)
        tit = read.get_metadata("DC", "title")
        if tit:
            return tit[0][0]
        else:
            return "no title available"
    else:
        print("Hmm, this file does not exist.")
        return
