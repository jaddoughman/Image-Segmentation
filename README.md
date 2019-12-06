# Image Segmentation

Segmentation algorithm that uses an Optical Character Recognition (OCR) engine to segment images to area/line/word levels. 

### Prerequisites

* [Tesseract 4.0](https://github.com/tesseract-ocr/tesseract)

### Installing Tesseract 4.0

You can either [Install Tesseract via pre-built binary package](https://github.com/tesseract-ocr/tesseract/wiki) or [build it from source](https://github.com/tesseract-ocr/tesseract/wiki/Compiling).

Supported Compilers are:

* GCC 4.8 and above
* Clang 3.4 and above
* MSVC 2015, 2017, 2019

Other compilers might work, but are not officially supported.


### Running Code

Change directory to the folder containing the image to be segmented. The goal now is to use Tesseract 4.0 to generate an XHTML version of the image, which contains the bounding box coordinates of every text line involved.

```
tesseract Sample.tif Sample hocr
```

The next step is to feed the image and its respective XHTML file to *segmentation.py* script, which will parse the the XHTML file and saving the cropped regions to the "Output" directory.

```
python3 segmentation.py --image Sample.tif --hocr Sample.xml
```
