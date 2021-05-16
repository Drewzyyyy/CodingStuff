import cv2
import numpy as np
from StackImages import stackImages

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i)
        if area>500:
            cv2.drawContours(imgCtr,i,-1,(255,0,0),3)
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            objCorners = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objCorners == 3: objType = "Triangle"
            elif objCorners == 4:
                ratio = w/float(h)
                if ratio > 0.95 and ratio < 1.05: objType = "Square"
                else: objType = "Rectangle"
            elif objCorners > 4: objType = "Circle"
            else: objType = "Unknown"

            cv2.rectangle(imgCtr,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imgCtr,objType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)

img = cv2.imread("Images/shapes.png")
imgCtr = img.copy()
blank = np.zeros_like(img)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

cv2.imshow("Images",stackImages(0.7,([img,imgGray,imgBlur],[imgCanny,imgCtr,blank])))

cv2.waitKey(0)