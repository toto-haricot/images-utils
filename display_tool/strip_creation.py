"""This module presents the core function of the display tool. create_a_strip() will generate a numpy array composed of 
the input images along with the corresponding outputs and the zooms. Then plot_stripes_into_pdf() will iteratively write
those arrays inside the PDFs
"""

# ---------- IMPORTS ---------------------------------------------------------------------------------

import os
import cv2

import numpy as np

from itertools import groupby
from image_utils import central_crop, draw_text_on_image, zooming_crop
from display_tool import *
from functions import * 

# ---------- FUNCTION TO CREATE A STRIP ---------------------------------------------------------

def create_a_strip(an_image_path:str, display_info=False):
    """This function will create a grand numpy array that contains an input image along with the corresponding outputs
    side to side. Just bellow each image a zoom is plotted. 

    Args:
        an_image_path (str): path to an image for inputs folder
        display_info (bool, optional): if you want all information on the way. Defaults to False.

    Returns:
        np.array: array containing all images and zooms. Ready to be saved into a PDF page
    """


    bg_color = (255,255,255)
    titles_color = (0,0,0)

    if display_info: print(f'Start building strip for image : {an_image_path} \n')
    
    output_image_paths = get_output_images_paths(an_image_path, display_tool.output_folders)

    #if no matching version is found we return False
    if len(output_image_paths) == 0:
        print(f'No matching version found for image {os.path.basename(an_image_path)}\n')
        return None

    # lists initialization
    input_image = cv2.imread(an_image_path)

    images = [input_image]
    shapes = [input_image.shape]
    pixels = [input_image.shape[0]*input_image.shape[1]]
    folders_name = [os.path.basename(os.path.dirname(an_image_path))]

    # list filling based on output_images_path
    for an_output_path in output_image_paths:

        img = cv2.imread(an_output_path)
        images.append(img)
        shapes.append(img.shape)
        pixels.append(img.shape[0]*img.shape[1])
        folders_name.append(os.path.basename(os.path.dirname(an_output_path)))

    if display_info:
        
        print(f'all folders name : {folders_name}')
        print(f'images shapes : {shapes}')
        print(f'number of pixels per image : {pixels}\n')

    # we check if there is any rotated image
    if is_there_rotated_image(shapes): 
        print(f'\n[WARNING] There is a rotated image in restored versions of {os.path.basename(an_image_path)}\n')
        for i, a_shape in enumerate(shapes[1:]):
            if (shapes[0][0] == a_shape[1]) and (shapes[0][1] == a_shape[0]):
                images[i+1] = cv2.rotate(images[i+1], cv2.ROTATE_90_CLOCKWISE)
                shapes[i+1] = shapes[0]


    # we check if all images have the same lengths and crop if necessary
    if not all_equal(shapes):

        if display_info: print('Not all shapes are equal, time for some central cropping... \n')

        cropped_images = []
        min_pos = pixels.index(min(pixels))
        standart_width, standart_height, _ = shapes[min_pos]

        for i, image_to_crop in enumerate(images):

            if display_info: print(f'[BEFORE CROP] image {i} has shape {images[i].shape}')

            cropped_image = central_crop(image_to_crop, standart_width, standart_height)
            cropped_images.append(cropped_image)

            if display_info: print(f'[AFTER CROP] image {i} has shape {cropped_image.shape} \n')

        images_to_plot = cropped_images

    else:

        if display_info: print('All shapes are equal, we are good to start plotting!\n')
        images_to_plot = images

    # let's add the zooming crop below each image
    h, w, c = images_to_plot[0].shape
    
    gap_v = int(0.1*w)
    gap_h = int(0.1*h)

    margin_h = np.ones((gap_h, w, c), dtype=int)
    margin_h = np.multiply(margin_h, bg_color).astype(int)

    margin_v = np.ones((2*h+gap_h, gap_v, c), dtype=int)
    margin_v = np.multiply(margin_v, bg_color).astype(int)

    for i, an_image in enumerate(images_to_plot):

        cropped_image = zooming_crop(img=an_image, crop_style='center')

        if display_info: 

            print(f'CONCATENATION OF IMAGE WITH ITS CROP BELLOW')
            print(f'upper image shape : {an_image.shape}')
            print(f'horizontal margin shape : {margin_h.shape}')
            print(f'cropped image shape : {cropped_image.shape}\n')

        cropped_image = cropped_image.astype(int)
        an_image= an_image.astype(int)

        images_to_plot[i] = cv2.vconcat([an_image, margin_h, cropped_image])

    # now we can hconcat them
    final_image = images_to_plot[0].astype(int)

    for image_to_plot_with_crop in images_to_plot[1:]:

        if display_info: 

            print(f'CONCATENATION OF IMAGE_AND_CROPS WITH ITS NEIGHBORS')
            print(f'left image shape : {final_image.shape}')
            print(f'vertical margin shape : {margin_v.shape}')
            print(f'right image shape : {image_to_plot_with_crop.shape}\n')
            final_image = final_image.astype(int)

        image_to_plot_with_crop = image_to_plot_with_crop.astype(int)

        final_image = cv2.hconcat([final_image, margin_v, image_to_plot_with_crop])

    if display_info: print('horizontal concatenation of all images done')

    # let's add a header to write algo names as titles
    header = np.ones((h//5, final_image.shape[1], c), dtype=int)
    header = np.multiply(header, bg_color).astype(int)

    if display_info: print(f'Header shape : {header.shape}\n')
    if display_info: print(f'Final image shape : {final_image.shape}\n')

    final_image = cv2.vconcat([header, final_image])
    
    y_title = header.shape[0]//2

    for i in range(len(images)):

        title = folders_name[i]
        x_title = (w + gap_v)*i + w//2
        draw_text_on_image(final_image, title, pos=(x_title, y_title),
                           text_color = titles_color, text_color_bg = bg_color,
                           font_scale=h//400)

    # let's add a global title
    final_image = cv2.vconcat([header, final_image])

    x_main_title = final_image.shape[1] // 2
    main_title = os.path.basename(an_image_path)

    draw_text_on_image(final_image, main_title, pos=(x_main_title, y_title), font_scale=h//400)

    return final_image
