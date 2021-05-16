import cv2
import numpy as np

img = cv2.imread("Images/Comrade_doggo.jpg")
print("Orig image size: ",img.shape)
imgResized = cv2.resize(img,(300,500))
print("Resized image size: ",imgResized.shape)
imgCropped = img[0:500,0:300] #img[height,width]
print("Cropped image size: ",imgCropped.shape)

cv2.imshow("Orig Image",img)
cv2.imshow("Resized Image",imgResized)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)