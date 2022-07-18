"""This module provides useful functions operating in the display_tool
"""

import os
import cv2

import numpy as np

from itertools import groupby
from image_utils import central_crop, draw_text_on_image, zooming_crop

# ----------------------------------------------------------------------------------------------------

def all_equal(iterable):
    """This function will tell if every element of an iterable are equal or not

    Args:
        iterable (_type_): list, dict, tuple, set

    Returns:
        boolean: True or False depending if all elements are equal or not
    """
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

# ----------------------------------------------------------------------------------------------------

def is_image(an_image:str):
    '''This function will return True or False if the path to a given image given represents an image or not
    
    Args:
        an_image (str): the path or basename of a file

    Returns:
        boolean: True or False depending if the image ends with '.png', '.jpg', '.JPG', '.jpeg' or '.JPEG'
    '''
    extensions = ['.png', '.jpg', '.JPG', '.jpeg', '.JPEG']
    if os.path.splitext(an_image)[1] in extensions:
        return True
    return False
    
# ----------------------------------------------------------------------------------------------------

def is_there_rotated_image(images_shapes:list):
    """This function will tell if in a given list of shapes there is any rotated image or not. 

    Args:
        images_shapes (list): A list of RGB images shapes

    Returns:
        Boolean: True or False depending on if a rotated image is found or not
    """
    assert all_equal(list(map(lambda x: len(x), images_shapes))), 'the images shapes do not have the same lengths'

    h, w, c = images_shapes[0]

    for a_shape in images_shapes[1:]:
        if a_shape[0] == w and a_shape[1] == h:
            return True
    
    return False

# ----------------------------------------------------------------------------------------------------

def n_images_folder(my_folder_path:str, is_image_function):
    """This function counts the number of images present in a given folder. It only detects images that ends with '.png', '.jpg', '.JPG', '.jpeg' or '.JPEG'

    Args:
        my_folder_path (str): path to folders in which we want to count the number of images
        is_image_function (bool): function used to assess if a file is an image or not

    Returns:
        int: numbeer of images in my_folder_path
    """

    if not os.path.isdir(my_folder_path) : 

        print(f'[ERROR] {my_folder_path} is not a directory, cannot count the number of images in n_images_folder() function')
        exit

    images = os.listdir(my_folder_path)
    n_images = sum(map(is_image_function, images))
    return n_images

# ----------------------------------------------------------------------------------------------------

def delete_none_image(images_list:str, print_n_deleted=False):
    is_an_images_list = list(map(is_image, images_list))
    all_images_list = [i for i in is_an_images_list if i != False]
    if print_n_deleted: 
        n_images_deleted = len(is_an_images_list) - len(all_images_list)
        print(f'function delete_none_image deleted {n_images_deleted} file(s)')
    return(all_images_list)

# ----------------------------------------------------------------------------------------------------

def neighbor_dirs(my_folder_path:str, print_warning=False):
    '''This function returns the number of repositories located at the same location as the input.
    At the same time it checks that all neighbors repositories have the same number of images as the input'''
    n_folders = 0
    upper_folder_path = os.path.split(my_folder_path)[0]
    neighbors_folders = []
    n_images = n_images_folder(my_folder_path, is_image)
    for a_folder in os.listdir(upper_folder_path):
        a_folder_path = os.path.join(upper_folder_path, a_folder)
        if os.path.isdir(a_folder_path) and a_folder_path != my_folder_path:
            n_folders += 1
            neighbors_folders.append(a_folder_path)
            folder_n_images = n_images_folder(a_folder_path, is_image)
            if (n_images != folder_n_images) and (print_warning is True):
                print(f'\n[WARNING] folder {a_folder} has {folder_n_images} images but input folder has {n_images}\n')
    return(n_folders, neighbors_folders, n_images)

# ----------------------------------------------------------------------------------------------------

def get_restored_images_paths(input_image:str):

    '''This function returns the paths of restored image corresponding to the input image'''

    restored_images_paths = []

    image_folder_path, input_image_basename = os.path.split(input_image)

    input_image_basename = os.path.splitext(input_image_basename)[0]

    restored_folders = neighbor_dirs(image_folder_path)[1]

    for restored_folder in restored_folders:

        all_restored_images = os.listdir(restored_folder)

        matching_restored_image = list(filter(lambda x: input_image_basename in x, all_restored_images))

        if len(matching_restored_image) == 0 :

            return []

        else: 

            restored_images_paths.append(os.path.join(restored_folder, matching_restored_image[0]))

    return(restored_images_paths)

# ----------------------------------------------------------------------------------------------------


