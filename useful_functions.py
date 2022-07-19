    """This python module define some useful functions that can be used in different projects. 
    """

# --------------- IMPORTS ----------------------------------------------------------------------------

import os
import cv2

import numpy as np

# --------------- COLOR SPACES -----------------------------------------------------------------------

def rgb_to_ycbcr(image_rgb : np.array):
    """This function translates a RGB image to YCbCr color space 

    Args:
        image_rgb (np.array): numpy array of an image in RGB color space

    Returns:
        np.array: numpy array of the input image converted to YCbCr color space
    """
    
    transition_mat = np.array([[.299, .587, .114],
                               [-.1687, -.3313, .5],
                               [-.5, .4187, -.0813]])

    image_ycrcb = image_rgb.dot(transition_mat.T) 
    image_ycrcb[:,:,[1,2]] += 128

    return image_ycrcb.astype(int)


def ycbcr_to_rgb(image_ycbcr : np.array):
    """This function translates a YCbCr image to RGB color space

    Args:
        image_ycbcr (np.array): input numpy array of an image in YCbCr color space

    Returns:
        np.array: numpy array of the input image converted to YCbCr color space
    """

    transition_mat = np.array([[1, 0, 1.402],
                               [1, -.34414, -.71414],
                               [1, 1.772, 0]])

    image_rgb = np.zeros(image_ycbcr.shape, dtype=np.uint8)
    image_rgb[:,:,[1,2]] -= 128
    image_rgb = image_ycbcr.dot(transition_mat.T)

    return image_rgb.astype(int)

# --------------- FILE MODIFICATIONS -----------------------------------------------------------------

def is_image(an_image:str):
    """This function will return False or a string if the path to image given in argument represent an image

    Args:
        an_image (str): The basename or path to a file, supposedly an image

    Returns:
        _type_: Either a string with the input image name or False if the file is not an image
    """

    extensions = ['.png', '.jpg', '.JPG', '.jpeg', '.JPEG']

    if os.path.splitext(an_image)[1] in extensions:
        return an_image
    return False

def remove_not_image(images_list:str, print_n_removed=False):
    """This function will parse all elements in a given list and keep only strings that refer to an image

    Args:
        images_list (str): _description_
        print_n_removed (bool, optional): _description_. Defaults to False.

    Returns:
        list: New list extracted from input images list with only the image files
    """
    is_an_images_list = list(map(is_image, images_list))
    all_images_list = [i for i in is_an_images_list if i != False]
    if print_n_removed: 
        n_images_removed = len(is_an_images_list) - len(all_images_list)
        print(f'{n_images_removed} file(s) detected as not image')
    return(all_images_list)


