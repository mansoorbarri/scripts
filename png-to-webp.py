# Import the Image module from the Python Imaging Library (PIL) 
from PIL import Image

#!/usr/bin/env python3

# ASCII art
a = '''
 +-++-++-++-+ +-++-+ +-++-++-++-++-++-++-+ +-++-++-++-++-+
 |c||o||d||e| |b||y| |M||a||n||s||o||o||r| |B||a||r||r||i|
 +-++-++-++-+ +-++-+ +-++-++-++-++-++-++-+ +-++-++-++-++-+
'''
print(a)

# Import the os and sys modules to work with files and directories
import os
import sys

# Define a function named "convert_png_to_webp"
def convert_png_to_webp():
    # Get the input path and output path from the command line arguments
    input_path = '/home/anar/Downloads/main.png'
    output_path = '/home/anar/Documents/GitHub/mani/website/public/images' + sys.argv[1] + "/main.webp"
    
    # Use the "os.path.abspath" method to get the absolute path of the input and output paths
    input_abs_path = os.path.abspath(input_path)
    output_abs_path = os.path.abspath(output_path)

    # Use the "with" statement to open the input PNG file using the Image module from PIL 
    # and store it in a variable named "img"
    with Image.open(input_path) as img:
        # Use the "save" method to save the opened image as a WebP file 
        # and store it in the output path specified by the user 
        img.save(output_path, 'webp')
        print("✓ converted successfully")

    # Delete the input image file
    os.remove(input_path)
    print("✓ image deleted")


# Call the "convert_png_to_webp" function to execute the code 
convert_png_to_webp()
