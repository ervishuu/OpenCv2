import cv2
import numpy as np
img= cv2.imread("F:/Images/f1.jpg")
cv2.imshow("original img",img)
cv2.waitKey(0)

#create 3x3 Kernal
kernal_3x3 = np.ones((3,3),np.float32)/9

blurred = cv2.filter2D(img,-1,kernal_3x3)
cv2.imshow("3x3 kernal img",blurred)
cv2.waitKey(0)
#create 7x7 Kernal
kernal_7x7= np.ones((7,7),np.float32)/49
#7x7 kernal
blurred2 = cv2.filter2D(img,-1,kernal_7x7)
cv2.imshow("7x7 kernal img",blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()