# Images2PDF
A short and sweet way to turn a series of images into a PDF file. One  image per page.

Drag-and-drop images onto the executable icon to generate a PDF, where each page is a single, uncompressed image. Works with one or more images. Should support any image file format [supported by PIL](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html), including PNG, JPEG, TIFF, and others. Each PDF page size may be different, depending on the provided image sizes.

Animated GIFs are not supported.

---

## Installation

Optionally, create a new virtual environment, such as with `venv` or `conda`:
```commandline
conda create -n images2pdf
conda activate images2pdf
```

Get the source and build the executable. 
- `$EXE_NAME` is the filename of the built executable, such as `img2pdf` or `DROP_IMGS_HERE`.
- `$DIST_PATH` is where the built executable will be deposited. It can be any path, like `path/to/exe/location` or `C:\Users\<username>\Desktop`.

```commandline 
git clone https://github.com/IndigoMaster/Images2PDF.git
cd Images2PDF
pip install -r requirements.txt
pyinstaller --onefile --name $EXE_NAME --distpath $DIST_PATH converter.py
```

---

## Usage

This utility does not have a command line interface or a GUI.
1. Select one or more image files in your file explorer.
2. Drag and drop the selected files onto the executable's icon.
3. A `Save-As` dialog will pop up, asking you for the name and location of the generated PDF file.
4. The PDF will be generated and saved in the desired location.
5. If there are any errors, they will be displayed in a terminal window.
