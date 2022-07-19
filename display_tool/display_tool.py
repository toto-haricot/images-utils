"""This python script is some sort of the main file. It enables to launch the display tool on an input folder if 
output folders are saved at the same location by calling functions from other files. 

The command line should be such as: 

    python display_tool.py --inputs_folder path/to/inputs --output_pdf_path path/to/where/writting/the/pdfs 
    --zoom "any_option"

"""

# ---------- IMPORTS ---------------------------------------------------------------------------------

import os
import cv2
import argparse

import matplotlib.pyplot as plt

from strip_creation import create_a_strip
from save_to_pdf import plot_stripes_into_pdf
from image_utils import central_crop, zooming_crop
from functions import *

# ---------- ARGUMENTS PARSING -----------------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument('--inputs_folder', type=str, required=True, help="path to folder with input images")
parser.add_argument('--output_pdf_path', type=str, required=True, help="path to folder to write PDFs")
parser.add_argument('--zoom', default="center", required=True, help="way to crop the images to get the zoom")

args = parser.parse_args()

global inputs_folder_path, output_path, zoom_option

inputs_folder_path = args.inputs_folder
output_path = args.output_pdf_path
zoom_option = args.zoom

# ---------- LAUNCHING MAIN  -------------------------------------------------------------------------

if __name__ == "__main__": 

    # global variables
    global n_folders, neighbors, n_images

    n_folders, neighbors, n_images = neighbor_dirs(inputs_folder_path, print_warning=True)

    input_images = os.listdir(inputs_folder_path)

    print(f'Launching display_tool on input folder {inputs_folder_path}\n')
    print(f'\tNumber of restored folder : {n_folders}')
    print(f'\tRestored folders are located at : {neighbors}')
    print(f'\tEach folder has {n_images} images \n')
    print(f'--------------------------------------------------\n')

    # PDFs creation
    plot_stripes_into_pdf(inputs_folder_path, pdf_output_path=output_path)
