# ---------- IMPORTS ---------------------------------------------------------------------------------

import os
import scipy
import argparse
import numpy as np

# ---------- FUNCTIONS TO COMPUTE BLOCKINESS ---------------------------------------------------------

def to_1d_signal(an_image:np.array, axis=0):

    shape = an_image.shape

    if axis==0:
        for i in range(1, shape[0]):
            an_image[-i,:] = abs(an_image[-i,:] - an_image[-i-1,:])
        print(an_image)
        an_image[0,:] = 0
        print(an_image)
        signal_1d = an_image.flatten('C')

    elif axis==1:
        for j in range(1, shape[0]):
            an_image[:,-j] = abs(an_image[:,-j] - an_image[:,-j-1])
        print(an_image)
        an_image[:,0]
        print(an_image)
        signal_1d = an_image.flatten('F')

    return(signal_1d)


def make_segments(signal, N):
    input_sequence = list(signal)
    n_segments = len(input_sequence)//N + 1
    segments = [input_sequence[N*i:N*(i+1)] for i in range(n_segments)]
    return segments


# ---------- MAIN ------------------------------------------------------------------------------------
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--image_path', type=str, required=True, help='path to folder with input images')

    args = parser.parse_args()

    image_path = args.image_path




