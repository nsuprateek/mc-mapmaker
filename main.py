import pandas as pd
from wand.image import Image

# Open an image
with Image(filename='input.jpg') as img:
    # Convert the image to the CIELAB color space
    img.colorspace = 'lab'

    # Save the CIELAB image
    img.save(filename='output_lab.jpg')

df = pd.read_csv('/home/suprateek/Minecraft mods/MC Map maker/mc_colors.csv')
# print(df)
import os
print(os.getcwd())


# img.
    

