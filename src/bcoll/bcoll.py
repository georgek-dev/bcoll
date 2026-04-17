import sys
from pathlib import Path

import art
from rich import print

from bcoll.config import *
from bcoll.epubparse import epfields, eptitle

# pdf- and epub-handling are in separate files; let's import them here
from bcoll.pdfparse import fields, title


def main():
    # I have no idea why I implemented the config rn
    if not exists():
        create()
        print("creating config")

    if len(sys.argv) < 2:
        print("Usage: bcoll [-v | --verbose] [--version] <BOOK>")
        return

    if "--version" in sys.argv:
        print("[yellow]bcoll[/yellow] version [green]0.0.1[/green]")
        return

    art.tprint("bcoll")
    verbose = "-v" in sys.argv or "--verbose" in sys.argv
    arg = [a for a in sys.argv[1:] if not a.startswith("-")]
    book = Path(arg[0])

    # let's determine between the EPUB and PDF file-types
    type = book.suffix.removeprefix(".")
    if verbose:
        print(f"book type: {type}")
    # now call the associated function
    if type == "pdf":
        if verbose:
            print(f"All fields for book [bold cyan]{book}[/bold cyan]")
            fields(book)
        print(f"Book title: {title(book)}")
    elif type == "epub":
        if verbose:
            print(f"All fields for book [bold cyan]{book}")
            epfields(book)
        print(f"Book title: {eptitle(book)}")


if __name__ == "__main__":
    main()
