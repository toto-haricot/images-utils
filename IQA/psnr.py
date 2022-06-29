import os
import cv2
import math
import argparse

import numpy as np
import pandas as pd

# -------------------- PARSING ARGUMENTS -------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument('--gt_folder', type=str, required=True, help='path to ground truth folder')
parser.add_argument('--restored_folder', type=str, required=False, help='path to folder with restored images')

args = parser.parse_args()

gt_folder = args.gt_folder
restored_folder = args.restored_folder

print(f'Launching PSNR computation for all images in {os.path.basename(gt_folder)}...\n')

# -------------------- USEFULL FUNCTIONS -------------------------------------------------------------

def is_image(image_path:str):
    """This function checks that the input folder image path (str) links to an image file and returns corresponding Boolean."""
    extensions = ['.png','.jpg','.JPG','.jpeg']
    if os.path.splitext(an_image)[1] in extensions: return image_path
    return False

def delete_none_images(input_list:list):
    """This function filter an input paths list to only keep images paths from that list and return the images paths list"""
    image_or_false = list(map(is_image,input_list))
    only_images = [i for i in image_or_false if i!=False]
    return(only_images)

def  make_pairs(gt_folder:str, restored_folder:str):
    """This function will create a list of tuples composed of each ground truth image along with its restored version"""    
    gt_folder = delete_none_images(os.listdir(gt_folder))
    restored_folder = delete_none_images(os.listdir(restored_folder))
    
    pairs = []

    assert len(gt_folder) == len(restored_folder), "Ground truths folder and Restored folder don't have the same length"

    for restored_image in restored_folder:

        corresponding_gt = list(map(lambda x: os.path.basename(restored_image) in x, gt_folder))

        assert len(corresponding_gt) == 1, "Restored image has no corresponding ground truth"

        gt_image = corresponding_gt[0]
        pairs.append((restored_image, gt_image))
    
    return(pairs)

def calculate_psnr(img1, img2):
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')
    return 20 * math.log10(255.0 / math.sqrt(mse))

# -------------------- MAIN --------------------------------------------------------------------------

results = {'restored_image': [],
        'gt_image' : [],
        'psnr' : []
        }

my_pairs = make_pairs(gt_folder, restored_folder)

for (img1, img2) in my_pairs:
    
    results['restored_image'].append(img1)
    results['gt_image'].append(img2)

    img1_path = os.path.join(restored_folder, img1)
    img2_path = os.path.join(gt_folder, img2)

    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)

    psnr = calculate_psnr(image1, image2)

    results['psnr'].append(psnr)

    print(f"Restored image : {img1}")
    print(f"Original image : {img2}")
    print(f"PSNR : {psnr}")

    print("_____________________________________________________________________")

df = pd.DataFrame(results)
df.to_csv(f"psnr.csv")

