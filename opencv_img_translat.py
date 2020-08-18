import cv2
import numpy as np
img= cv2.imread("F:/Images/f1.jpg")

#store height and weight
height , width = img.shape[:2]
print(height)
print(width)

quarter_height , quarter_width = height/4 , width/4
print(quarter_height)
print(quarter_width)

T = np.float32([[1,0,quarter_width],
                [0,1,quarter_height]])
print(T)

img_translation = cv2.warpAffine(img,T,(width,height))
cv2.imshow("Original Image",img)
cv2.imshow("Translation  Image",img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()