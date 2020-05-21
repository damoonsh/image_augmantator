from PIL import Image
import math

# Create a new image with the given size
def create_image(height, width):
    image = Image.new("RGB", (height, width))
    return image

img = Image.open('images/Cat00.jpg');
height, width = img.size
newImg = create_image(height, width)
pixels = newImg.load()

for x  in range(height - 2):
    for y in range(width - 2):
        avgRed, avgBlue, avgGreen = 0, 0, 0
        for ix in range(3):
            for iy in range(3):
                avgRed += img.getpixel((x + ix, y + iy))[0]
                avgGreen += img.getpixel((x + ix, y + iy))[1]
                avgBlue += img.getpixel((x + ix, y + iy))[2]
        print(avgBlue)
        pixels[x][y] = (int(avgRed / 9), int(avgGreen / 9), int(avgBlue / 9))

newImg.show()