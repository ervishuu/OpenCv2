import cv2
img=cv2.imread("F:/Images/f1.jpg")
cv2.imshow("Original Image",img)

cv2.imwrite("output.jpg",img)
cv2.imwrite("output.png",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
