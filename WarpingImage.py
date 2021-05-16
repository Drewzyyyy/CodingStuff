import cv2
import numpy as np

img = cv2.imread("Images/Comrade_doggo.jpg")

width,height = 250,350
pts1 = np.float32([[240,20],[381,20],[240,136],[381,136]]) #Upper Left, Upper Right, Lower Left, Lower Right
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(img,matrix,(width,height))

print(img.shape)

cv2.imshow("Image",img)
cv2.imshow("Warped Image",imgOut)

cv2.waitKey(0)