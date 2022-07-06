# images_utils :hammer_and_wrench:

This package provides functionalities to ease images handling for computer vision projects, written in python.  

In this repository you will find the following python scripts : 

- **display_tool/** : This tool aims to help visualizing the outputs of an algorithm along with the corresponding inputs. More information is available in **display_tool/readme.md**

`python display_tool/display_tool.py --inputs_folder *path/to/inputs* --output_pdf_path *path/to/folder/for/pdf/printing*`


- **IQA/** : In this repository you will find several scripts for Image Quality Assessment. 


- **crop_central.py** : This python file enables to central crop all images in a given input folder if their shapes exceed a certain width and height. The cropped images are saved into the given output directory. 

`python central_crop.py --folder_path *path/to/images* --output_dir *path/to/folder/to/save/images* --width_max *maximum_width* --height_max *maximum_height*`


- **crop_select.py** : This file will allow you to crop an image based on the selection you will input when script launched. 

`python crop_select.py --image_path *path/to/image*`


- **histogram_equalization.py** : to enhance the contrast of an image, equalizing its histogram might be a good alternative. This script will output an histogram equalized image corresponding to the given input

`python histogram_equalization.py --image_path *path/to/image*`
