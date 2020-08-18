import cv2
import numpy as np
img= cv2.imread("F:/Images/f1.jpg")
cv2.imshow("Original img",img)
cv2.waitKey(0)

# blure img
blur = cv2.blur(img,(3,3))
cv2.imshow("blured img",blur)
cv2.waitKey(0)

# using Box Filter
gaussian = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gaussian Blur img",gaussian)
cv2.waitKey(0)

#median blur
median = cv2.medianBlur(img,5)
cv2.imshow("median img",median)
cv2.waitKey(0)


# Bilatory fillter
bilateral = cv2.bilateralFilter(img,9,90,90)
cv2.imshow("Bilateral img",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
