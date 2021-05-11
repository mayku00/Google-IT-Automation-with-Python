#!/usr/bin/env python3
from PIL import Image
import os

images_path = "supplier-data/images/"
list_images = os.listdir(images_path)
image_size = (600, 400)

for image in list_images:
    if 'tiff' in image:
        # grab the picture name without the .tiff extension
        file_name = os.path.splitext(image)[0]
        outfile = "supplier-data/images/" + file_name + ".jpeg"
        try:
            # first convert RGBA 4-channel format to RGB 3-channel format before processing the images.
            Image.open(images_path + image).convert("RGB").resize(image_size).save(outfile, "JPEG")
        except IOError:
            print("cannot convert", image)
