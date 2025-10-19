# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of 
# the image to some other place, count the used colors in the image

import cv2
import numpy as np # we will need numpy for some array manipulations

# Loading images in grey and color and store them in the variables 'img_gray' and 'img_color'.
img_gray = cv2.imread("tutorials/data/images/logo.png",cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("tutorials/data/images/logo.png",cv2.IMREAD_COLOR)


# Check if images have been loaded successfully.
if img_gray is None:
    raise FileNotFoundError("image not found")
if img_color is None:
    raise FileNotFoundError("image not found")

## Image data access

#  Do some print out about the loaded data using 'type', 'dtype' and 'shape'.
print(type(img_gray))
print(type(img_color))

print(img_gray.dtype)
print(img_color.dtype)

print(img_gray.shape)
print(img_color.shape)

#  Continue with the grayscale image by copying it to a new variable 'img'.
img = img_gray.copy()

# Extract the size or resolution of this image.
height, width, = img_gray.shape
print(height)
print(width)

## This is how you can access the height and width of an image stored as a numpy ndarray. 
## In all following exercises you should use this way to access the height and width of an image.
## Then, you can use the variables 'height' and 'width' in your code instead of hardcoding values. 
## This makes your code flexible and independent from the actual image size.

# Resize the image to a small size (7x5) as we will later print out the pixel values.

img_small = cv2.resize(img, (7,5))

cv2.imwrite("img_small.jpg", img_small)
cv2.imshow("img_small", img_small)
# HINT: Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for 
# general access on ndarrays

# Print first row
print(img[0])

# Print first column
print(img[:, 0])

#  Now continue with the color image by copying it to the variable 'img'.
img = img_color.copy()


# Set an area of the image to black by looping over the pixels and setting the pixel values to [0,0,0].
for y in range(100):
    for x in range(50):
        img[y,x] = [0,0,0]
cv2.imshow("black_area", img)
#  Create a window with 'namedWindow' and show the image and wait until key pressed.
title = "Bild"
cv2.namedWindow(title)
# TODO Find all used colors in the image by first reshaping the image to a list of pixels with 'reshape' 
# (which is a numpy function that can be applied to images as they are stored as 'ndarrays').

# TODO Use 'np.unique' to find all unique colors in the reshaped image. Use the parameter 'axis=0' to
# search for unique rows (pixels) instead of unique single values.

# TODO Copy one part of an image into another one by first defining a region of interest (ROI) and then storing 
# the data in a temporal variable before copying it to another part of the image.

#  Save the image to a file using 'imwrite'.
cv2.imwrite("output.jpg", img_gray)
#  Load the image again and show it in a window.
cv2.imshow("img", img_gray)

cv2.waitKey(0)
# TODO Show the original image in another window to illustrate the effect of the copy operation. Check
# if you have used 'copy' or if you just stored a reference to the original image using the '=' operator.
