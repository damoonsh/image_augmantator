from PIL import Image
import numpy as np
import pandas as pd
import cv2 as cv

def open_image(image_name, path='images/'):
    return Image.open(path + image_name)

# Create a new image with the given size
def create_image(height, width):
  image = Image.new("RGB", (height, width), 0)
  return image


def gray_scale(img, wR=0.299, wG=0.587, wB=0.114):
    """
        Returns the gray scale version of a given image.

        # Arguments:
            img: ndarray of images passed along with (height, with, channel) shape
            wR, wG, wB: weights for RGB values that are default but could be set

        # Returns:
            the new image
    """
    height, width, s = img.shape
    data_type = img.dtype
    new_img = np.zeros((height, width, s), dtype=data_type)

    for x in range(0, height):
        for y in range(0, width):
            new_pixel_value = int(wR * img[x, y, 0] + wG * img[x, y, 1] + wB * img[x, y, 2])
            new_img[x, y] = [new_pixel_value, new_pixel_value, new_pixel_value]

    return new_img

def get_rgb(path_to_image, root_path='./images/'):
    """ 
    Given a path to an image it will return a dictionary containing the 
    rgb pixels values with values RED, GREEN, BLUE.
    
    # Params:
        path_to_image: the image's path
        root_path: origing of images, default is set to the images folder
    
    # Returns:
        A dictionary containign RGB values of an image
    """
    pixels = cv.imread(root_path + path_to_image)

    RED = pd.DataFrame(pixels[:,:,0])
    GREEN = pd.DataFrame(pixels[:,:,1])
    BLUE = pd.DataFrame(pixels[:,:,2])

    dictionary = {"R": RED, "G": GREEN, "B": BLUE}

    return dictionary

def convert_pixel_to_df(pixelList, height, width):
    length = height * width
    
    red, green, blue = [], [], []

    for l in range(length):
        R, G, B = pixelList[l]

        red.append(R)
        green.append(G)
        blue.append(B)

    newShape = (width, height)

    red = np.reshape(red, newShape)
    green = np.reshape(green, newShape)
    blue = np.reshape(blue, newShape)

    return red, green, blue

