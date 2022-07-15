"""_summary_
"""

# --------------- IMPORTS ----------------------------------------------------------------------------

import os
import cv2
import argparse

import pandas as pd

from useful_functions import is_image, remove_not_image

# --------------- PARSING ARGUMENTS -------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', type=str, required=True)
args = parser.parse_args()

folder_path = args.folder_path

# --------------- XXXXXXX XXXXXXXXX -------------------------------------------------------------------

def manage_image_folder(folder_path:str, df:pd.DataFrame):

    all_images = os.listdir(folder_path)
    all_images = remove_not_image(all_images, print_n_removed=True)

    prefixe = os.path.basename(folder_path)

    for idx, image_name in enumerate(all_images):

        image_name_no_space = image_name.replace(" ","_")

        os.system(f"mv '{os.path.join(folder_path, image_name)}' '{os.path.join(folder_path, image_name_no_space)}'")

        image_name = image_name_no_space

        suffixe = '_' + '0'*(4-len(str(idx+1))) + str(idx+1) 
        extension = os.path.splitext(image_name)[1]
        image_new_name = prefixe + suffixe + extension

        image_path = os.path.join(folder_path, image_name)
        image_path_new = os.path.join(folder_path, image_new_name)

        print(f'image_path : {image_path}')
        print(f'image_path_new : {image_path_new}')

        img = cv2.imread(image_path)
        image_size = img.shape

        image_info_df = pd.DataFrame({'img_name': [image_new_name], 'old_name': [image_name], 'size': [image_size]})
        
        os.system(f'rm {image_path}')
        cv2.imwrite(image_path_new, img)
        df = pd.concat([df,image_info_df], ignore_index=True, axis=0)

        print(f'--------------------------------------------------')

    return df

# --------------- MAIN --------------------------------------------------------------------------------

if __name__ == '__main__':

    df = pd.DataFrame(columns=['img_name','old_name','size'])

    df = manage_image_folder(folder_path, df)

    df.to_csv(os.path.join(folder_path, os.path.basename(folder_path) + ".csv"), index=False)














