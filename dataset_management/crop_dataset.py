# ------------------------------------------------------------------------------------------
# ----- IMPORTS ----------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

import os
import cv2
import tqdm
import argparse

import numpy as np


# ------------------------------------------------------------------------------------------
# ----- ARGUMENT PARSING -------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument('--input_folder', type=str, required=True, help="path to folder with bmp images")
parser.add_argument('--output_folder', type=str, required=True, help="path to folder to save png images")

args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder

image_extensions = ['.png', '.jpg', '.JPG', '.jpeg', '.JPEG']


# ------------------------------------------------------------------------------------------
# ----- FUNCTIONS FOR MAIN() ---------------------------------------------------------------
# ------------------------------------------------------------------------------------------

def central_crop(image:np.array, width:int, height:int):
    """This function will center crop an image to given width and height
    Args:
        image (np.array): image read in a numpy array
        width (int): cropping dimensions
        height (int): cropping dimensions
    Returns:
        np.array: image cropped to given dimensions
    """
    h, w, c = image.shape
    x_margin, y_margin = (h - height)//2, (w - width)//2
    return image[x_margin:x_margin+height, y_margin:y_margin+width,:]


def resize_image(image_path:str, output_path:str, height:int=1200, width:int=1600):
    """This function central crops an image to given height and width and save it
    to the output_path given as argument
    Args:
        image_path (str): path to read image
        output_path (str): path to save image
        height (int): cropping dimension
        width (int): cropping dimension
    """
    image = cv2.imread(image_path)
    image = central_crop(image, height, width)
    if not cv2.imwrite(output_path, image):
        print(f"error resize {image_path} // {output_path}")


def resize_folder(input_folder:str, output_folder:str, height:int=1200, width:int=1600):
    """This function will resize a whole folder containing images and save the
    images to another given folder output folder. 

    Args:
        input_folder (str): _description_
        output_folder (str): _description_
        height (int): cropping dimension
        width (int): cropping dimension
    """
    for a_file in tqdm.tqdm(os.listdir(input_folder)):

        if os.path.splitext(a_file)[1] in image_extensions:
            image_path = os.path.join(input_folder, a_file)
            output_path = os.path.join(output_folder, a_file)
            resize_image(image_path, output_path, height=1200, width=1600)

        else: print(f"{a_file} detected as not image")


# ------------------------------------------------------------------------------------------
# ----- MAIN() -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

def main():

    if not os.path.isdir(input_folder): 
        raise Exception(f"{input_folder} is not a directory")

    if not os.path.isdir(output_folder):

        print(f"{output_folder} directory does not exist")
        print(f"creating {output_folder}...")
        os.mkdir(output_folder)

    resize_folder(input_folder, output_folder)

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

    









