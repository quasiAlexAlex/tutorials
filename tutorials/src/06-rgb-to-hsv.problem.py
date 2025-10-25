# Tutorial #6
# -----------
#
# Playing around with colors. We convert some values from RGB to HSV and then find colored objects in the image and mask
# them out. Includes a color picker on double-click now. The RGB version is meant to demonstrate that this does not work
# in RGB color space.

import numpy as np
import cv2

# Print keyboard usage
print("This is a HSV color detection demo. Use the keys to adjust the \
selection color in HSV space. Circle in bottom left.")
print("The masked image shows only the pixels with the given HSV color within \
a given range.")
print("Use h/H to de-/increase the hue.")
print("Use s/S to de-/increase the saturation.")
print("Use v/V to de-/increase the (brightness) value.\n")
print("Double-click an image pixel to select its color for masking.")

# Capture webcam image
cap = cv2.VideoCapture(0)

# Get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))

print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Codec = " + str(codec))

# Drawing helper variables
thick = 10
thin = 3
thinner = 2
font_size_large = 3
font_size_small = 1
font_size_smaller = 0.6
font = cv2.FONT_HERSHEY_SIMPLEX

# Define  RGB colors as variables
red = 100
green = 50
blue = 20

# Exemplary color conversion (only for the class), tests usage of cv2.cvtColor

# Enter some default values and uncomment
hue = 100
hue_range = 10
saturation = 100
saturation_range = 100
value = 100
value_range = 100


# Callback to pick the color on double click
def color_picker(event, x, y, flags, param):
    global hue, saturation, value
    if event == cv2.EVENT_LBUTTONDBLCLK:
        (h, s, v) = hsv[y, x]
        hue = int(h)
        saturation = int(s)
        value = int(v)
        print("New color selected:", (hue, saturation, value))
    
orig_win = "original"
cv2.namedWindow(orig_win, cv2.WINDOW_GUI_NORMAL)
cv2.setMouseCallback(orig_win, color_picker)


while True:
    # Get video frame (always BGR format!)
    ret, frame = cap.read()
    if ret:
        # Copy image to draw on
       
        img = frame.copy()

        # Compute color ranges for display

        lower = np.array([hue - hue_range, saturation - saturation_range, value - value_range])
        upper = np.array([hue + hue_range, saturation + saturation_range, value + value_range])

        # Draw selection color circle and text for HSV values

        img = cv2.circle(img, (width -50, height -50), 50, (blue, green, red), -1 )
        
        #  Convert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        #  Create a bitwise mask

        mask = cv2.inRange(hsv, lower, upper)

        # Apply mask

        masked_img = cv2.copyTo(img, mask=mask)

        # Show the original image with drawings in one window

        cv2.imshow(orig_win, img)

        #  Show the masked image in another window

        cv2.imshow("masked", masked_img)

        # Show the mask image in another window

        cv2.imshow("mask", mask)

        #  Deal with keyboard input

        key = cv2.waitKey(10)
        if key == ord("q"):
            break
        
    else:
        print("Could not start video camera")
        break

cap.release()
cv2.destroyAllWindows()
