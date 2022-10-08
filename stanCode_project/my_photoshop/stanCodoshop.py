"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_dist = math.sqrt((pixel.red-red)**2+(pixel.green-green)**2+(pixel.blue-blue)**2)
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_red = 0
    total_green = 0
    total_blue = 0
    avg_list = []      # A list of average red, green, and blue values of the pixels.
    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue
    avg_list.append(total_red // len(pixels))
    avg_list.append(total_green // len(pixels))
    avg_list.append(total_blue // len(pixels))
    return avg_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg = get_average(pixels)
    dist_list = []  # A list of "color distance" between a pixel and a mean RGB value.
    best = []       # A list of RGB value of the pixel having smallest color distance.
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        dist_list.append(dist)
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if dist == min(dist_list):
            best = pixel
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            pixels = []  # A list of pixels at (x, y) from different images.
            for image in images:
                img_p = image.get_pixel(x, y)
                pixels.append(img_p)
            best = get_best_pixel(pixels)
            result_p = result.get_pixel(x, y)
            result_p.red = best.red
            result_p.green = best.green
            result_p.blue = best.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
