import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# img[:] = 255,0,0
# print(img)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),3) #(Source,Starting Point, Ending Point, Color, Thickness)
cv2.rectangle(img,(0,0),(250,350),(255,255,0),6)
cv2.circle(img,(400,50),30,(0,255,0),2) #(Source,Center,Radius, Color, Thickness)
cv2.putText(img," OPENCV ",(300,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),3) #(Source, Text, Origin, Font, Scale, Color, Thickness)

cv2.imshow("Zeros",img)
cv2.waitKey(0)