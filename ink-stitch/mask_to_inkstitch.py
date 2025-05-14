# -*- coding: utf-8 -*-
"""
Script takes masked or flat coloured images where the colours or masks
represent a unique stitch type. and outputs .svg files for Inkscape.
The file may be used as a tool extension of the ink-stitch plugin to automate
the choice of stitch type for matching a given stitch in the input file.
"""

from PIL import Image
import numpy as np
import sys
import cv2  # OpenCV for connected component analysis
import os
import svgwrite
from skimage import measure

### This has not quite worked -- leaves  alot of regions empty at 0 for some reason

def mask_col_to_svg(mask_path, output_prefix):
    # Load the images
    mask_img = Image.open(mask_path)
    
    if "\\" in output_prefix:
        directory_path = '\\'.join(output_prefix.split('\\')[0:-1])
        os.makedirs(directory_path, exist_ok=True)
    
    # Convert image to numpy arrays
    mask_array = np.array(mask_img)
    height, width, _ = mask_array.shape
    
    # Initialize SVG file
    dwg = svgwrite.Drawing(f"{output_prefix}.svg", profile='tiny', size=(width, height))
    
    # Find unique colors in the mask (ignoring the background)
    unique_colors = np.unique(mask_array.reshape(-1, mask_array.shape[2]), axis=0)
    background_color = np.array([0, 0, 0]) # Background colour
    
    #greyscale_masks = np.zeros_like(mask_array).astype(np.uint16)
    mask_area_threshold = 100
    for color in unique_colors:
        if not np.array_equal(color, background_color):
            mask = (mask_array == color).all(axis=2).astype(np.uint8)  # May need to convert to uint8 for OpenCV
            # Perform connected component analysis
            num_labels, labels_im = cv2.connectedComponents(mask)
            for label in range(1, num_labels):  # Label 0 is the background
                component_mask = labels_im == label#1 # only use largest mask
                
                
                if np.sum(component_mask) > mask_area_threshold:
                    # Find contours of the component
                    contours = measure.find_contours(component_mask, 0.5)
                    
                    for contour in contours:
                        # Create an SVG path from the contour
                        path_data = "M " + " L ".join([f"{x[1]},{x[0]}" for x in contour]) + " Z"
                        path = dwg.path(d=path_data, fill=svgwrite.rgb(*color, mode='RGB'), stroke='none')

                        # Add path to the SVG file
                        dwg.add(path)

    # Save the SVG file
    dwg.save()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: script.py [input.png] [output.svg]")
        sys.exit(1)
    
    img_in = sys.argv[1]
    output = sys.argv[2]

    mask_col_to_svg(img_in, output)