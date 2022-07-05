# --------------- IMPORTS ----------------------------------------------------------------------------

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

# --------------- IMAGE EDITING -----------------------------------------------------------------------

