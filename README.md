# images_utils  ⚒️

This package provides functionalities to ease images handling for computer vision projects, written in python.

In this repository you will find the following python scripts : 

## repositories 📦

- 📁 **display_tool/** : This tool aims to help visualizing the outputs of some algorithms along with the corresponding inputs. It is especially usefull for benchmarks. More information is available in **display_tool/readme.md**. </br></br>

- 📁 **images_comparison/** : In this repository you will find several scripts to measure the proximity and similarity between two images. This is a type **Image Quality Assessment** algorithms for which we always have the ground truth, in this case we say that we are dealing with full-reference iqa. </br></br>

## scripts 📋

- 📝 **crop_central.py** : This python script enables to central crop all images in a given input folder if their shapes exceed a certain width and height. The cropped images are saved into the given output directory.

`python central_crop.py --folder_path *path/to/images* --output_dir *path/to/folder/to/save/images* --width_max *maximum_width* --height_max *maximum_height*` </br></br>


- 📝 **crop_select.py** : This file will allow you to crop an image based on the selection you will input when script launched. 

`python crop_select.py --image_path *path/to/image*` </br></br>


- 📝 **dataset_cleaning.py** : this script will look at all images in the given *folder_path* and rename all images with the following standard `foldername_000XX.png`. The script also outputs a csv file that contains all images former names and new ones along with the images sizes. 

`python dataset_cleaning.py --folder_path *path/to/folder*` </br></br>


- 📝 **histogram_equalization.py** : to enhance the contrast of an image, equalizing its histogram might be a good alternative. This script will output an histogram equalized image corresponding to the given input

`python histogram_equalization.py --image_path *path/to/image*` </br></br>

# Requirements ☝️

All required python packages to run any script from this repository are listed in `requirements.txt`. We advice using `Python3`. </br></br>
