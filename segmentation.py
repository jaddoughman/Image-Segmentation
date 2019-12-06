import xml.etree.ElementTree as ET
import argparse
import os
from PIL import Image

def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)

def createFolder(directory):
    """
    @param directory: name of directory to be created
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def segment(input_file_name,xml_file_name,crop_level):
    """
    @param input_file_name: name of input image
    @param xml_file_name: name of input xml file
    @param crop_level: level of cropping (area/paragraph/line/word)
    """
    createFolder("Output")
    tree = ET.parse(xml_file_name)
    root = tree.getroot()

    count = 1
    # Parsing HOCR file to get bounding box coordinates
    if crop_level=="ocr_par":
        tag = 'p'
    elif crop_level=="ocr_line" or crop_level=="ocrx_word":
        tag = 'span'
    elif crop_level=="ocr_carea":
        tag = 'div'
  
    rootiter = "{http://www.w3.org/1999/xhtml}" + tag
    for span in root.iter(rootiter):
        if(span.get('class')==(crop_level)):
            s = span.get('title')

            # Splitting bounding box string into coordinates
            semicolon = s.split(";")[0]
            x1 = int(semicolon.split(" ")[1])
            y1 = int(semicolon.split(" ")[2])
            x2 = int(semicolon.split(" ")[3])
            y2 = int(semicolon.split(" ")[4])

            segment_file_name = crop_level + "_" + str(count) + ".jpg"
            path_to_new_folder = "Output/" + segment_file_name

            width = int(x2-x1)
            height = int(y2-y1)
            prop = float(width/height)

            # Image Coordinates Out of Bounds Handler
            if(x1!=0): #and (width>height) and (height<100) and (prop>10)):
                crop(input_file_name, (x1, y1, x2, y2), path_to_new_folder)

            count = count + 1

def main():
    parser = argparse.ArgumentParser(description='Image and HOCR file')
    parser.add_argument('image', type=str, help='Input image file')
    parser.add_argument('hocr', type=str, help='Input HOCR file')
    parser.add_argument('level', type=str, help='Area/paragraph/line/word level')
    args = parser.parse_args()
    
    segment(args.image,args.hocr,args.level)
    
if __name__ == '__main__':
    main()
