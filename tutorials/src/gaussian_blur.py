import cv2
import numpy as np





# Bild laden
img = cv2.imread('tutorials/data/images/sift_table01.jpg', cv2.IMREAD_GRAYSCALE)

# Rauschparameter
mean = 400          # Median
stddev = 255        # Standardabweichung

# Rauschen erzeugen
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)

# Rauschen hinzufügen
noisy_img = cv2.add(img, noise)

# Speichern und anzeigen
cv2.imwrite('gaussian_img.jpg', noisy_img)
cv2.imshow("Gaussian_img", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
