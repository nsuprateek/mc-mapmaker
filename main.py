import pandas as pd
from PIL import Image as img
from math import sqrt
# from scipy import skimage

def rgb_to_cielab(rgb):

    R = ( rgb[0] / 255 )
    G = ( rgb[1] / 255 )
    B = ( rgb[2] / 255 )
    
    # Converting to range(0,100)
    if R > 0.04045:
        R = ((R + 0.055) / 1.055) ** 2.4
    else:
        R = R / 12.92
    if G > 0.04045:
        G = ((G + 0.055) / 1.055) ** 2.4
    else:
        G = G / 12.92
    if B > 0.04045:
        B = ((B + 0.055) / 1.055) ** 2.4
    else:
        B = B/12.92

    R = R * 100
    G = G * 100
    B = B * 100

    # Matrix multiplication to CIE XYZ
    X = R * 0.4124 + G * 0.3576 + B * 0.1805
    Y = R * 0.2126 + G * 0.7152 + B * 0.0722
    Z = R * 0.0193 + G * 0.1192 + B * 0.9502

    # Division by reference point (D65 2 degree)
    X = X / 95.047
    Y = Y / 100.00
    Z = Z / 108.883

    # Conversion to CIE LAB
    if X > 0.008856:
        X = X ** (1/3)
    else:
        X = (7.787 * X) + (16 / 116)
    if Y > 0.008856:
        Y = Y ** (1/3)
    else:
        Y = (7.787 * Y) + (16 / 116)
    if Z > 0.008856:
        Z = Z ** (1/3)
    else:
        Z = (7.787 * Z) + (16 / 116)

    CIE_L = ( 116 * Y ) - 16
    CIE_a = 500 * ( X - Y )
    CIE_b = 200 * ( Y - Z )

    return [CIE_L, CIE_a, CIE_b]

def find_closest():
    pass

df = pd.read_csv('/home/suprateek/Minecraft mods/MC Map maker/mc_colors.csv')
# print(df)
import os
print(os.getcwd())
with img.open('test.png') as i:
    i.show()

# img.
    

