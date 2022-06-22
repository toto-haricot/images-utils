import os
import cv2
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages
from strip_creation import create_a_strip
from functions import false_if_not_image, delete_none_image
 
def plot_stripes_into_pdf(inputs_folder_path:str, pdf_output_path:str = None):
    """This function will parse the inputs folder and for each image 
        (i) create the result strip thanks to strip_creation.py 
        (ii) save this strip into a new page of a PDF results
        (iii) save the PDF asa it reaches 50 pages

    Args:
        inputs_folder_path (str): path to the inputs directory
        pdf_output_path (str, optional): _description_. Defaults to None.
    """

    all_input_images = delete_none_image(os.listdir(inputs_folder_path))

    main_folder_name = os.path.basename(os.path.split(inputs_folder_path)[0])
    pdf_output_path = os.path.join(pdf_output_path, main_folder_name)

    N = len(all_input_images)
    print(f'{N} images to process in total...\n')

    n_pdf = 1
    n_pages_max = 50
    n_pdf_total = (N//n_pages_max+1)
    
    while n_pdf < n_pdf_total+1:

        n_pages = 0

        pdf_name = pdf_output_path+f'{n_pdf}'+'.pdf'

        pp = PdfPages(pdf_name)

        print(f'Start writting pdf number {n_pdf}')

        while (n_pages < n_pages_max) and ((n_pdf-1)*n_pages_max+n_pages < N):

            image_number = (n_pdf - 1)*50 + n_pages

            input_image = all_input_images[image_number]

            input_image_path = os.path.join(inputs_folder_path, input_image)

            image_strip = create_a_strip(input_image_path, display_info=False)
            
            if image_strip is None:
                n_pages += 1
                continue

            image_strip_rgb = image_strip[:,:,::-1]
            fig = plt.figure(figsize=(40, 15))
            plt.imshow(image_strip_rgb)
            plt.axis('off')
            
            plt.savefig(pp, format='pdf', bbox_inches='tight', dpi=200)

            print(f'PDF {n_pdf} / {n_pdf_total} page {n_pages+1} / {n_pages_max}')

            n_pages += 1

        pp.close()

        print(f'Just finish writting pdf number {n_pdf} \n')

        n_pdf += 1









    # while n_pages < n_pages_max:



    # for index, image_image in enumerate(all_input_images):






    #     if i%50 < 50

    # if pdf_output_path:
    #     pp = PdfPages(pdf_output_path)

    # for input_image in all_input_images:
    #     input_image_path = os.path.join(inputs_folder_path, input_image)
    #     image_strip = create_a_strip(input_image_path, display_info=False)
    #     image_strip_rgb = image_strip[:,:,::-1]
    #     fig = plt.figure(figsize=(40, 15))
    #     plt.imshow(image_strip_rgb)
    #     plt.axis('off')
    #     if pdf_output_path:
    #         plt.savefig(pp, format='pdf', bbox_inches='tight', dpi=200)
    # if pdf_output_path:
    #     pp.close()

