# images_utils  ⚒️

This package provides functionalities to ease images handling for computer vision projects, written in python.

In this repository you will find the following python scripts : 

## modules 📦

- 📁 **display_tool/** : This tool aims to help visualizing the outputs of some algorithms along with the corresponding inputs. It is especially usefull for benchmarks. More information is available in **display_tool/readme.md**. </br></br>

- 📁 **IQA/** : In this repository you will find several scripts for **Image Quality Assessment**. You will find implementation of full reference image quality assessment algorithms (PSNR, SSIM), blind iqa algorithms (blockiness) and some metrics to evaluate the performances of an iqa scoring algorithme with respect to human assessment. More information is available in **iqa/readme.md**. </br></br>

## scripts 📋

- 📝 **crop_central.py** : This python script enables to central crop all images in a given input folder if their shapes exceed a certain width and height. The cropped images are saved into the given output directory.

`python central_crop.py --folder_path *path/to/images* --output_dir *path/to/folder/to/save/images* --width_max *maximum_width* --height_max *maximum_height*` </br></br>


- 📝 **crop_select.py** : This file will allow you to crop an image based on the selection you will input when script launched. 

`python crop_select.py --image_path *path/to/image*` </br></br>


- 📝 **histogram_equalization.py** : to enhance the contrast of an image, equalizing its histogram might be a good alternative. This script will output an histogram equalized image corresponding to the given input

`python histogram_equalization.py --image_path *path/to/image*` </br></br>
