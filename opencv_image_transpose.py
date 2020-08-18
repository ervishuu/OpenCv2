import cv2
import numpy as np
img= cv2.imread("F:/Images/f1.jpg")
rotated_img = cv2.transpose(img)

cv2.imshow("Original Img",img)
cv2.imshow("ROtated Img",rotated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()