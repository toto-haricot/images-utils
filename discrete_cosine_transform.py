# ----------------------------------------------------------------------------------------------------
# ---------- IMPORTS ---------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------
# ---------- FUNCTIONS -------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

def plot_dct_frequency_basis(block_size:int=8):
    """This function will save the frequency elementary basis on which
    an image can be decompose during a Discrete Cosine Transform.
    Args:
        block_size (int, optional): Size of the block. Defaults to 8.
    """
    rows = np.arange(0,block_size,1).reshape((1,block_size))
    cols = np.arange(0,block_size,1).reshape((block_size,1))

    plt.figure(figsize=(block_size*2, block_size*2))

    for u in rows[0,:]:
        for v in cols[:,0]:

            ax = plt.subplot(8,8,u*8+v+1)

            term1 = np.cos(cols*pi*u/(2*block_size))  
            term2 = np.cos(rows*pi*v/(2*block_size))
            freq = term1 @ term2

            ax.set_axis_off()
            ax.imshow(freq, cmap='gray')

    plt.savefig('./frequency_basis.png')


