import cv2
img=cv2.imread("F:/Images/f1.jpg")
cv2.imshow("Original Image",img)

print(img.shape)
print("Height pixel value:" ,img.shape[0])
print("Weight pixel value:" ,img.shape[1])


cv2.waitKey(0)
cv2.destroyAllWindows()