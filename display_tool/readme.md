# Was is the display_tool 💡

This repository was created to help analysis the results of a benchmark between different algorithms dealing with images. Imagine you have 200
images in the folder `inputs/` and you want to compare the outputs that different models, let's say `algo1`, `algo2`... `algoN` give when ran on
all images of `inputs/`. If you store the outputs of the N algorithms in N folders, the **display_tool** will create some PDFs that contain on each
page one of the input images and the corresponding outputs of the different algorithmes. <br> <br>

Along with the stripes created, made of the input and the outputs of each algorithm, you can get a zoom in each image to have more details. This is
done thanks the `--zoom *zooming_option*` argument that is per default set to *center*. What means that it will plot just bellow each image a center
crop of the images. <br> <br>

Here comes an illustration of the overall operating of **display_tool** : <br>

# How to use display_tool 📝
