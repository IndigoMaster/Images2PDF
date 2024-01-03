import sys
from pathlib import Path
from typing import List

from PIL import Image
from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog


def convert_images_to_pdf(image_paths: List[Path], output_path: Path) -> None:
    """
    Generate a PDF file. Each page of the PDF is an image.
    Images not resized or compressed. Each PDF page may be
    a different size.

    :param image_paths: list of paths to images to add to PDF
    :param output_path: PDF destination location
    :return: None
    """
    pdf = FPDF(unit="mm")
    for image_path in image_paths:
        image = Image.open(image_path)
        width, height = image.size
        # Convert image size from pixels to millimeters (1 pixel = 0.264583 mm)
        width_mm, height_mm = width * 0.264583, height * 0.264583
        # Set PDF page size to image size
        pdf.add_page(orientation='P', format=(width_mm, height_mm))
        # Add image to page at full size
        pdf.image(image_path, 0, 0, width_mm, height_mm)
    pdf.output(str(output_path))


def handle_drop(files):
    root = tk.Tk()
    root.withdraw()  # We don't need a full GUI, so keep the root window from appearing
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF file", "*.pdf")])
    if output_path:
        convert_images_to_pdf(files, Path(output_path))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            handle_drop(sys.argv[1:])
        except Exception as e:
            print(e)
            input('\n\nPress ENTER to close...')
    else:
        print("Drag and drop images onto the app icon. No CLI or GUI.")
