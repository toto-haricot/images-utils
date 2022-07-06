"""This python script enables to central crop all images in a folder if their width or height exceed 
some given limits. 

All images are then copy pasted to an output directory, which then stores all cropped images. 

If an image from the input folder has a shape which is bellow the given limits, it will be simply
copy pasted.
"""

 # --------------- IMPORTS ----------------------------------------------------------------------------

import os
import cv2
import argparse

from tqdm import tqdm

# --------------- PARSING ARGUMENTS -------------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument('--folder_path', type=str, required=True, help='path to images folder')
parser.add_argument('--output_dir', type=str, required=True, help='new repository to save cropped images')
parser.add_argument('--width_max', type=int, required=True, help='max image width before central cropping')
parser.add_argument('--height_max', type=int, required=True, help='max image height before central cropping')

args = parser.parse_args()

folder_path = args.folder_path
output_dir = args.output_dir
width_max = args.width_max
height_max = args.height_max

input_folder_basename = os.path.basename(folder_path)
output_dir_basename = os.path.basename(output_dir)

# --------------- CODE --------------------------------------------------------------------------------

i = 0
j = 0

print(f"\n\nLaunching central_crop python file with parameters : \n")
print(f"\twidth maximal : {width_max}")
print(f"\theight maximal : {height_max} \n")

# let's check that the output folder exists and if not lets create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f'Start processing folder {folder_path}...\n')

# we parse all elements in the input folder
for image_name in tqdm(os.listdir(folder_path), desc=f'Parsing {input_folder_basename}: '):

    image_extension = os.path.splitext(image_name)[1]
    image_basename = os.path.splitext(image_name)[0]

    if image_extension not in ['.jpg', '.jpeg', '.png', '.JPG']:

        print(f'\nFile detected as not image : {image_name}. Just passing by...')
        print(f'\n-------------------------------------------------- \n')

        continue

    image_path = os.path.join(folder_path, image_name)

    image = cv2.imread(image_path)

    width_image, height_image, channels = image.shape

    if (width_image <= width_max+1) and (height_image <= height_max+1):
        
        os.system(f'cp {image_path} {output_dir}')

        j += 1

        continue

    x_center, y_center = width_image//2, height_image//2

    # if the image is wider AND higher than the maximal sizes
    if (width_image > width_max+1) and (height_image > height_max+1):

        x_margin, y_margin = (width_image - width_max)//2, (height_image - height_max)//2

        cropped_image = image[x_margin:-x_margin, y_margin:-y_margin, :]

        cropped_image_name = image_basename + '_cc' + image_extension

        if cv2.imwrite(os.path.join(output_dir, cropped_image_name), cropped_image):
            i += 1

    # if the image is only wider but less high than the maximal sizes
    elif (width_image > width_max+1) and (height_image <= height_max+1):

        x_margin = (width_image - width_max)//2

        cropped_image = image[x_margin:-x_margin,:,:]

        cropped_image_name = image_basename + '_cc' + image_extension

        if cv2.imwrite(os.path.join(output_dir, cropped_image_name), cropped_image):
            i += 1

    # if the image is only higher but less width than the maximal sizes
    elif (width_image <= width_max+1) and (height_image > height_max+1):

        y_margin = (height_image - height_max)//2

        cropped_image = image[:,y_margin:-y_margin,:]

        cropped_image_name = image_basename + '_cc' + image_extension

        if cv2.imwrite(os.path.join(output_dir, cropped_image_name), cropped_image):
            i += 1

print(f'\nProcessing over. \n\t{i} images cropped.\n\t{j} image(s) just copied pasted.\n\n')


# ----------------------------------------------------------------------------------------------------