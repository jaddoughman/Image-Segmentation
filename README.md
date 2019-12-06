# Image Segmentation

Segmentation algorithm that uses an Optical Character Recognition (OCR) engine to segment images to area/paragraph/line/word levels. Initially, the image needs to be passed through Tesseract 4.0, Google's open source OCR engine, to generate an *hocr* file containing the bounding box coordinates of every area, paragraph, line, and word in the image. The image file and the hocr file are then passed to *segmentation.py* , which parses the XHTML file and saves the every cropped image in the *Output* directory. 

### Prerequisites

* [Tesseract 4.0](https://github.com/tesseract-ocr/tesseract)

### Installing Tesseract 4.0

You can either [Install Tesseract via pre-built binary package](https://github.com/tesseract-ocr/tesseract/wiki) or [build it from source](https://github.com/tesseract-ocr/tesseract/wiki/Compiling).

Supported Compilers are:

* GCC 4.8 and above
* Clang 3.4 and above
* MSVC 2015, 2017, 2019

Other compilers might work, but are not officially supported.


### Generating HOCR file

Change directory to the folder containing the image to be segmented. The goal now is to use Tesseract 4.0 to generate an XHTML version of the image, which contains the bounding box coordinates of every text line involved.

```
tesseract Sample.tif Sample hocr
```

### Segmenting Image To Area/Paragraph/Line/Text Level

The next step is to feed the image and its respective XHTML file to *segmentation.py* script, which will parse the the XHTML file and saving the cropped regions to the *Output* directory.

**Segmenting Image to Area Level**
```
python3 segmentation.py Sample.tif Sample.hocr ocr_carea
```

**Segmenting Image to Paragraph Level**
```
python3 segmentation.py Sample.tif Sample.hocr ocr_par
```

**Segmenting Image to Line Level**
```
python3 segmentation.py Sample.tif Sample.hocr ocr_line
```

**Segmenting Image to Word Level**
```
python3 segmentation.py Sample.tif Sample.hocr ocrx_word
```

Now, a new folder called *Output* has been created containing the cropped images.
