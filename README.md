# Image Segmentation Tessearct 4.0

Segmentation algorithm that uses Tesseract 4.0's OCR engine to segment input images to text/word/paragraph levels. 

Steps: 
  1) Generate HOCR file of your input image using Tesseract 4.0 [tesseract input_path output_path -l lang hocr]
  2) Rename output_file's extension from output.hocr to Sample.xml
  3) Rename input image to Sample.jpg/png/tif... 
  3) Place Sample.xml and Sample.jpg/png/tif in same directory as *segmentation.py*
  4) Run *segmentation.py* [python segmentation.py]
  
  
  
