import cv2
import numpy as np

image = cv2.imread("aaaa.jpg")

gray_avg = np.mean(image, axis=2).astype(np.uint8)

gray_luminance = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Wyświetlenie obrazów
cv2.imshow("Grayscale (Average)", gray_avg)
cv2.imshow("Grayscale (Luminance Method)", gray_luminance)
cv2.waitKey(0)
cv2.destroyAllWindows()