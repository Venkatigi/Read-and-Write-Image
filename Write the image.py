import cv2
a=cv2.imread('1.jpg',1)
cv2.imwrite("12.jpg",a)
cv2.imshow("car",a)
cv2.waitKey(0)