import cv2 as cv
import pandas as pd
import numpy as np
from utils import *

image = cv.imread('./images/Cat01.jpeg')

def get_saturation(value, quadrant):
    if value > 223:
        return 255
    elif value > 159:
        if quadrant != 1:
            return 255

        return 0
    elif value > 95:
        if quadrant == 0 or quadrant == 3:
            return 255

        return 0
    elif value > 32:
        if quadrant == 1:
            return 255

        return 0
    else:
        return 0


def convert_dithering(image, stride=2):
    # Get size
    width, height, channels = image.shape

    # Create new Image and a Pixel Map
    new = np.zeros((height, width, channels))

    # Transform to half tones
    for i in range(0, width, stride):
        for j in range(0, height, stride):
            # Get Pixels
            p1 = image[i, j]
            p2 = image[i, j + 1]
            p3 = image[i + 1, j]
            p4 = image[i + 1, j + 1]

            # Color Saturation by RGB channel
            red = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
            green = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
            blue = (p1[2] + p2[2] + p3[2] + p4[2]) / 4

            # Results by channel
            r = [0, 0, 0, 0]
            g = [0, 0, 0, 0]
            b = [0, 0, 0, 0]

            # Get Quadrant Color
            for x in range(0, 4):
                r[x] = get_saturation(red, x)
                g[x] = get_saturation(green, x)
                b[x] = get_saturation(blue, x)

            # Set Dithered Colors
            new[i, j] = (r[0], g[0], b[0])
            new[i, j + 1] = (r[1], g[1], b[1])
            new[i + 1, j] = (r[2], g[2], b[2])
            new[i + 1, j + 1] = (r[3], g[3], b[3])

        # Return new image
        return new

n = convert_dithering(image)

cv.imshow('main-one', image)
cv.imshow('test', gray_scaled)

cv.waitKey(0)
cv.destroyAllWindows()
