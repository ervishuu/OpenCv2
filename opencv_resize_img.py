import cv2
import numpy as np
img= cv2.imread("F:/Images/f1.jpg")
cv2.imshow("Original img",img)
cv2.waitKey(0)

#Resize
img_scaled = cv2.resize(img,None,fx = 2,fy =2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resize img ",img_scaled)
cv2.waitKey(0)


cv2.destroyAllWindows()