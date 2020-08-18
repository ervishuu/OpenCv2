import cv2
import numpy as np
img= cv2.imread("F:/Images/f1.jpg",0)
height , width = img.shape

#sobel extract
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow("Original img",img)
cv2.waitKey(0)

cv2.imshow("Sobel x",sobel_x)
cv2.waitKey(0)

cv2.imshow("Sobel y",sobel_y)
cv2.waitKey(0)



cv2.destroyAllWindows()