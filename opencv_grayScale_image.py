import cv2
img = cv2.imread("F:/Images/f1.jpg")
cv2.imshow("Original Img",img)
cv2.waitKey(0)
# Convert Gray Scale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray scale image",gray_img)
cv2.waitKey(0)


cv2.destroyAllWindows()