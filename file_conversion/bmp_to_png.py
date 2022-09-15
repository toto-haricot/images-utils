"""This script enables to convert all images in a given folder from a .bmp format .png
"""

# ------------------------------------------------------------------------------------------
# ----- IMPORTS ----------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

import os
import cv2
import tqdm
import argparse

# ------------------------------------------------------------------------------------------
# ----- CONVERSION FUNCTION ----------------------------------------------------------------
# ------------------------------------------------------------------------------------------

def conversion_bmp_to_png(input_folder:str, output_folder:str):

    # checking arguments
    if input_folder is None: raise Exception("[ERROR] Must input a folder path to bmp images")
    if output_folder is None: raise Exception("[ERROR] Must input a folder path to save images")

    # converting images
    for an_image in tqdm.tqdm(os.listdir(input_folder)):

        an_image_bn, an_image_ext = os.path.splitext(an_image)

        if an_image_ext in ['.bmp', '.BMP']: 
            image = cv2.imread(os.path.join(input_folder, an_image))
            output_path = os.path.join(output_folder, an_image_bn + '.png')
            if not cv2.imwrite(output_path, image): 
                print(f'error with saving {an_image}\n')

    print(f"Images from {input_folder} converted to .png and saved in {output_folder}")

# ------------------------------------------------------------------------------------------
# ----- MAIN -------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # argument parsing 
    parser = argparse.ArgumentParser()

    parser.add_argument('--folder_bmp', type=str, required=True, help="path to folder with bmp images")
    parser.add_argument('--folder_png', type=str, required=True, help="path to folder to save png images")

    args = parser.parse_args()

    folder_bmp = args.folder_bmp
    folder_png = args.folder_png

    # calling conversion function
    conversion_bmp_to_png(input_folder=folder_bmp, output_folder=folder_png)
