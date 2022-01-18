r"""
Routines for processing abstracts.
"""

import sys

from PyQt5.QtWidgets import QApplication

from PIL import Image

import typer

from biblio.gui.abstract.MainWindowApp import MainWindowApp

app = typer.Typer()


class Abstract:
    def __init__(self, text: str, image: Image):
        r"""
        Create a new abstract object with the given text and image.
        :param text: the abstract text.
        :param image: the abstract image.
        """

        self.text = text
        self.image = image


def abstract_gui(in_pdf_name: str):
    r"""
    Retrieve the abstract from a pdf file and return the abstract text and an image of
    the abstract.
    :param in_pdf_name: the input PDF file name.
    :param out_png_name: the output PDF file name.
    :return: an Abstract object.
    """

    app = QApplication(sys.argv)

    form = MainWindowApp()
    form.show()
    app.exec_()

    return Abstract(form.abstract_text, form.abstract_image)


@app.command()
def gui(in_pdf_name: str, out_png_name: str):
    r"""
    Process abstract information using a GUI.
    :param in_pdf_name: the name of the PDF file that contains the abstract.
    :param out_png_name: the name of the output PNG file that extracted PDF will be written to.
    :return: an Abstract object.
    :return: None
    """

    abstract = abstract_gui(in_pdf_name)

    if abstract.text is not None:
        print("Abstract text:")
        print(abstract.text)
    else:
        print("No abstract text given")

    if abstract.image is not None:
        abstract.image.save(out_png_name)
        print(f"Image saved to {out_png_name}")
    else:
        print("No image to save")
