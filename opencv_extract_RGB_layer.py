import cv2
import numpy as np

img = cv2.imread("F:/Images/f1.jpg")
cv2.imshow("Orignal img",img)
cv2.waitKey(0)
# Spilt img into three layer
B,G,R = cv2.split(img)
zeros = np.zeros(img.shape[:2],dtype='uint8')

#Red layer
cv2.imshow("red",cv2.merge([zeros,zeros,R]))
cv2.waitKey(0)
#Green Layer
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)
#Blue layer
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()