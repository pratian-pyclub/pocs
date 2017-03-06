#!/usr/bin/env python
"""

Consists of all the image operations.

"""
from PIL import Image

"""
Gives the average RGB color intensity in the given dimensions of the image.
Input params: Image, corner points to find the dimensions (minX,minY) to
(maxX,maxY). pixel_array if the image is already laoded.
Output: tuple of three float values representing RGB intensity in the image.

"""
def avg_color(image, minX, minY, maxX, maxY, pixel_array=None):
    if pixel_array==None:
        pixel_array = image.load()

    sum_counts = [0, 0, 0]
    pixels_counted = 0
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            # sum_counts += pixel_array[x, y]
            # three dimensions due to RGB.
            sum_counts[0] += pixel_array[x, y][0]
            sum_counts[1] += pixel_array[x, y][1]
            sum_counts[2] += pixel_array[x, y][2]
            pixels_counted += 1

    return [sum_counts[0]/pixels_counted, sum_counts[1]/pixels_counted, sum_counts[2]/pixels_counted]

"""
Gives 4x3 matrix of values representing the RGB values in each quadrant of
the image in the specified path
Input: image_path
Output: List of 12 float values

"""
def twelve_tone(image_path):
    image = Image.open(image_path)
    a = avg_color(image, 0, 0, image.size[0]/2, image.size[1]/2)
    b = avg_color(image, image.size[0]/2, 0, image.size[0], image.size[1]/2)
    c = avg_color(image, 0, image.size[1]/2, image.size[0]/2, image.size[1])
    d = avg_color(image, image.size[1]/2, image.size[1]/2, image.size[0],
    image.size[1])

    return [
        a[0], a[1], a[2],
        b[0], b[1], b[2],
        c[0], c[1], c[2],
        d[0], d[1], d[2]
    ]
