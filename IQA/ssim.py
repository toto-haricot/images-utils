import os
import cv2
import math
import glob
import argparse

import numpy as np
import pandas as pd

from skimage.metrics import structural_similarity as ssim

# -------------------- PARSING ARGUMENTS -------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument('--gt_folder', type=str, required=True, help='path to ground truth folder')
parser.add_argument('--restored_folder', type=str, required=False, help='path to folder with restored images')

args = parser.parse_args()

gt_folder = args.gt_folder
restored_folder = args.restored_folder
algo_name = args.algo

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

# -------------------- MAIN --------------------------------------------------------------------------

results = {'restored_image': [],
        'gt_image' : [],
        'ssim' : []
        }

my_pairs = make_pairs(gt_folder, restored_folder, algo_name)

for (img1, img2) in my_pairs:

    print(f"Restored image : {img1}")
    print(f"Original image : {img2}")
    
    results['restored_image'].append(img1)
    results['gt_image'].append(img2)

    img1_path = os.path.join(restored_folder, img1)
    img2_path = os.path.join(gt_folder, img2)

    image1 = cv2.imread(img1_path)
    image2 = cv2.imread(img2_path)

    measure = ssim(image1, image2, channel_axis=2)

    results['ssim'].append(measure)

    print(f"SSIM : {ssim}")

    print("_____________________________________________________________________")

df = pd.DataFrame(results)
df.to_csv(f"{algo_name}_ssim.csv")

