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

def draw_text_on_image(img, text, pos=(20,20), font=cv2.FONT_HERSHEY_DUPLEX, 
                       font_scale=2, font_thickness=5, text_color=(10,10,10), 
                       text_color_bg=(255,255,255), text_bg_transparency=None):
    
    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    
    # if text_bg_transparency:
    #     holes = np.zeros_like(img)
    #     cv2.rectangle(img, (x - text_w, y - text_h), (x + text_w, y + text_h), text_color_bg, -1)
    #     cv2.rectangle(holes, (x - text_w, y - text_h), (x + text_w, y + text_h), (255,255,255), -1)
    #     mask = holes.astype(bool)
    #     img[mask] = cv2.addWeighted(img, text_bg_transparency, holes, 1-text_bg_transparency, 0)[mask]

    # else: 
    
    # cv2.rectangle(img, (x - text_w, y - text_h), (x + text_w, y + text_h), text_color_bg, -1)

    cv2.putText(img, text, (x - text_w//2, y + text_h//2 + font_scale - 1), font, font_scale, text_color, font_thickness)
