"""This python script enables to draw a rectangle on an image based on mouse click on two points.

The image with the rectangle will be saved in the same repository with same name ending with rectangle.
"""

# --------------- IMPORTS ----------------------------------------------------------------------------

import os
import cv2
import argparse

# --------------- PARSING ARGUMENTS -------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('--image_path', type=str, required=True)
args = parser.parse_args()

image_path = args.image_path

# --------------- CALLBACK FUNCTION -------------------------------------------------------------------

def draw_rectangle(event, x, y, flags, params):
    """This callback function will be used to draw a rectangle on an image based on the left click on image

    Args:
        event (_type_): listens to cv2 events, if matches left buttom down will go through the script
        x (_type_): first coordinate of the click
        y (_type_): second coordinate of the click
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if len(points) < 2:
        
            cv2.circle(img, (x, y), thickness, (0, 0, 255),-1)
            print('------------------------------')
            print(f'click on position ({x}, {y})')
            cv2.imshow('image', img)
            points.append((x, y))

        if len(points) == 2:

            cv2.rectangle(img, points[0], points[1], (0, 0, 255), thickness)
            print('------------------------------')
            print(f'Plotting rectangle between {points[0]} and {points[1]}')
            print('------------------------------')
            cv2.imshow('image_with_rectangle',img)
            if cv2.imwrite(os.path.join(folder_path, image_output_name), img):
                print(f'Image with rectangle saved as {image_output_name}')
            print('Please hit ESC to quit and save image_with_rectangle')


# --------------- MAIN --------------------------------------------------------------------------------

if __name__ == '__main__':

    img = cv2.imread(image_path)
    thickness = img.shape[0]//100

    image_name = os.path.basename(image_path)
    folder_path = os.path.dirname(image_path)
    image_bs, image_ext = os.path.splitext(image_name)
    image_output_name = image_name + '_rectangle' + image_ext

    points = []

    cv2.imshow('image', img)

    cv2.setMouseCallback('image', draw_rectangle)

    k = cv2.waitKey(0)

    if k == 27: 
        cv2.destroyAllWindows()
        print()

