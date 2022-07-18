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

inputs_folder_path = args.inputs_folder
output_path = args.output_pdf_path
zoom_option = args.zoom

# ---------- COUNT NUMBER OF RESULTS FOLDERS  --------------------------------------------------------

n_folders, neighbors, n_images = neighbor_dirs(inputs_folder_path, print_warning=True)

input_images = os.listdir(inputs_folder_path)

print(f'Number of restored folder : {n_folders} \n')
print(f'Restored folders are located at : {neighbors} \n')
print(f'Each folder has {n_images} images \n')

# ---------- LAUNCHING THE PDF CREATION --------------------------------------------------------------

print(f'inputs folder : {inputs_folder_path}')

plot_stripes_into_pdf(inputs_folder_path, pdf_output_path=output_path)
