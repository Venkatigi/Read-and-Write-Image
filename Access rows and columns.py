import cv2
a=cv2.imread('1.jpg',1)
import random
for i in range(100):
    for j in range(a.shape[1]):
        a[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imwrite('12.jpg',a)
cv2.imshow('nothing',a)
cv2.waitKey(0)