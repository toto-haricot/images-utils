# --------------- IMPORTS ----------------------------------------------------------------------------

import os
import cv2
import argparse

import numpy as np
import matplotlib.pyplot as plt

# --------------- PARSING ARGUMENTS -------------------------------------------------------------------

parser = argparse.ArgumentParser()

parser.add_argument('--image_path', type=str, required=True, help='path to image to histogram equalize')

args = parser.parse_args()

image_path = args.image_path

# --------------- USEFUL FUNCTIONS --------------------------------------------------------------------

def compute_histogram(image, bins:int=256):
    hist = np.zeros(bins)
    for pixel in image:
        hist[pixel]+=1
    return hist

def compute_cumulative_distribution(hist):
    a = iter(hist)
    b = [next(a)]
    for i in a: 
        b.append(b[-1] + i)
    return np.array(b)

# --------------- MAIN -------------------------------------------------------------------------------

if __name__ == "__main__":

    image_basename, image_ext = os.path.splitext(image_path)

    if image_ext not in ['.jpeg','.JPEG','.jpg','.JPG','.png']:
        
        print(f'[ERROR] {image_path} is not an image')
        
        quit
    
    image = cv2.imread(image_path)[:,:,0]

    image_flat = image.flatten()

    histogram = compute_histogram(image_flat)
    print(f'Histogram shape : {histogram.shape}\nHistogram value : {histogram}\n\n')
    cumulative = compute_cumulative_distribution(histogram)
    print(f'Cumulative shape : {cumulative.shape}\nCumulative value : {cumulative}\n\n')

    mx, mn = cumulative.max(), cumulative.min() 

    cumulative_normed = (cumulative - mn) * 255 / (mx - mn)
    cumulative_normed = cumulative_normed.astype('uint8')

    print(f'Cumulative normed shape : {cumulative_normed.shape}\nCumulative value : {cumulative_normed}\n\n')

    # now let's use the mapping defined by cumulative_normed
    image_he = cumulative_normed[image_flat]
    print(f'Image histogram equalized shape : {image_he.shape}\nImage histogram equalized value : {image_he}\n\n')
    print(f'Input image shape : {image.shape}')
    image_he = np.reshape(image_he, image.shape)

    fig = plt.figure(figsize=(20,5))

    fig.add_subplot(1,4,1)
    plt.imshow(image, cmap='gray')

    fig.add_subplot(1,4,2)
    plt.plot(histogram, color='blue')
    
    fig.add_subplot(1,4,3)
    plt.plot(cumulative_normed, color='red')

    fig.add_subplot(1,4,4)
    plt.imshow(image_he, cmap='gray')

    plt.show()



