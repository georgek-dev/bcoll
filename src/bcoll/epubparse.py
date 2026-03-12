from ebooklib import epub
from pathlib import Path
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

    print("[bold yellow]Warning:[/bold yellow] The -v book values are broken for epubs. [bold red]Use at your own risk.[/bold red]")
    print(f"Values of file [cyan]{book}[/cyan]")
    for ns, dat in md.items():
        for i in dat:    
            c = i[0] if isinstance(i, (tuple, list)) else i
            a = i[1] if isinstance(i, (tuple, list)) else i

            print(f"{ns} {c} {a}")

def eptitle(book):
    book = Path(book)
    
    if book.exists():
        read = epub.read_epub(book)
        tit = read.get_metadata('DC', 'title')
        if tit:
            return tit[0][0]
        else:
            return "no title available"
    else:
        print("Hmm, this file does not exist.")
        return
