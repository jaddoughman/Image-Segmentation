import xml.etree.ElementTree as ET
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
    @param directory: path of directory to be created
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def segment(sample_file_name,xml_file_name):
    sample_file_name_no_extension = sample_file_name.split(".")[0]
    createFolder(sample_file_name_no_extension)
    tree = ET.parse(xml_file_name)
    root = tree.getroot()

    count = 1
    # Parsing HOCR file to get bounding box coordinates
    for span in root.iter('{http://www.w3.org/1999/xhtml}span'):
        if(span.get('class')==('ocr_line')):
            s = span.get('title')

            # Splitting bounding box string into coordinates
            semicolon = s.split(";")[0]
            x1 = int(semicolon.split(" ")[1])
            y1 = int(semicolon.split(" ")[2])
            x2 = int(semicolon.split(" ")[3])
            y2 = int(semicolon.split(" ")[4])

            segment_file_name = "line_1_" + str(count) + ".jpg"
            path_to_new_folder = sample_file_name_no_extension + "/" + segment_file_name

            width = int(x2-x1)
            height = int(y2-y1)
            prop = float(width/height)

            # Image Coordinates Out of Bounds Handler
            if(x1!=0): #and (width>height) and (height<100) and (prop>10)):
                crop(sample_file_name, (x1, y1, x2, y2), path_to_new_folder)

            count = count + 1


segment("Sample.tif","Sample.xml")

