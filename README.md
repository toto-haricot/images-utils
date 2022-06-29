# images_utils

This package provides functionalities to ease images handling for computer vision projects, written in python.  

In this repository you will find the following python scripts : 

- **display_tool/** (repository) : This tool aims to help visualizing the outputs of an algorithm along with the corresponding inputs. 
The command line to launch the script is `python display_tool/display_tool.py --inputs_folder *path/to/inputs* --output_pdf_path *path/to/folder/for/pdf/printing*`. 
More information is available in **display_tool/readme.md**

- **central_crop.py** : This python file enables to central crop all images in a given input folder if their shapes exceed a certain width and height. The cropped images are saved into the given output directory. 
It can be used thanks to `python central_crop.py --folder_path *path/to/images* --output_dir *path/to/folder/to/save/images* --width_max *maximum_width* --height_max *maximum_height*`
