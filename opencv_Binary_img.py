import cv2
img = cv2.imread("F:/Images/f1.jpg",0)
cv2.imshow("Gray img",img)
cv2.waitKey(0)
#Thresholding method
ret,bw = cv2.threshold(img,127,250,cv2.THRESH_BINARY)
cv2.imshow("Binary img",bw)



cv2.waitKey(0)

cv2.destroyAllWindows()