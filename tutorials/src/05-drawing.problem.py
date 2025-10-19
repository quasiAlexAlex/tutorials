# Exercise #5
# -----------
#
# Create a white image and draw something on it.

import cv2
import numpy as np

# Create a white image of size 625x512 using the 'ones' function from numpy
width, height = 625, 512
img = np.ones((height, width, 3), np.uint8) * 255


## Drawing helper variables
# Thickness
thick = 10
thin = 3

# Colors in RGB
blue = (255, 0, 0) #<--- Fixme
red = (255, 0, 0)
darkgreen = (20, 200, 20)
black = (0, 0, 0)

# Fonts
font_size_large = 3
font_size_small = 1
font = cv2.FONT_HERSHEY_SIMPLEX

#  Create a window and display the image and jump to the last task and display the image for debugging 
# before you implement the drawing tasks

cv2.namedWindow("Bild")

# Draw a green diagonal cross over the image using 'line'

img = cv2.line(img, (0, 0), (width, height), darkgreen, thick)
img = cv2.line(img, (0, height), (width, 0), darkgreen, thick)

# Draw a circle using 'circle'

img = cv2.circle(img, (width - 100, 250), 50, red, cv2.FILLED, cv2.LINE_4)

# Write some text using 'putText'

img = cv2.putText(img, "?GDV!", (10, height - 10), font, font_size_large, red, thin)

# Draw arrows indicating a coordinate system using 'arrowedLine' and use 'putText' to label the axes

img = cv2.arrowedLine(img, (10, 10), (100, 10), blue, thin)
img = cv2.putText(img, "X", (115, 25), font, font_size_small, blue, thin)
img = cv2.arrowedLine(img, (10, 10), (10, 100), blue, thin)
img = cv2.putText(img, "Y", (5, 130), font, font_size_small, blue, thin)


# Display the image
cv2.imshow("Bild", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## FIXME there is a bug in this code, can you find it? Hint: It is related to the color definitions.

