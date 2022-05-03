import cv2
A=cv2.imread("1.jpg",1)
tag=A[250:350,275:290]
A[225:325,250:265]=tag
cv2.imshow("Car",A)
cv2.waitKey(0)