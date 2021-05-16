import cv2
import numpy as np
import keyboard as kb
import mouse
import pyautogui as pg
from StackImages import stackImages

vid = cv2.VideoCapture(0)
vid.set(3,1280)
vid.set(4,720)
vid.set(10,150)

myColors = [142,97,0,179,255,255] # hue_min, saturation_min, value_min, hue_max, saturation_max, value_max
chosen_color = [0,0,0]
myPoints = [] #[x,y]

draw = False

def getColor(img,colors):
    newPoints = []
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array(myColors[0:3])
    upper = np.array(myColors[3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    x,y=getContours(mask)
    cv2.circle(imgRes,(x,y),39,colors,cv2.FILLED)
    if x!=0 and y!=0:
        newPoints.append([x,y,colors])
    return newPoints

def drawOnCanvas(myPoints):
    for point in myPoints:
        cv2.circle(imgRes,(point[0],point[1]),30,point[2],cv2.FILLED)


def empty(a):
    pass

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x = y = w = h = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area>500:
            # cv2.drawContours(imgRes,i,-1,(255,0,0),3)
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

while True:
    success, img = vid.read()
    x, y = pg.position()
    colors = pg.pixel(x, y)

    if draw:
        cv2.putText(img,"Select color",(0,40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
        cv2.circle(img,(100,40), 15, colors, -1)
        if kb.is_pressed('space'):
            draw = False
            chosen_color = colors

    cv2.putText(img,"Text state: {}".format(draw),(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    # imgRes = cv2.bitwise_and(img,img,mask=mask)
    imgRes = img.copy()
    newPoints = getColor(img,chosen_color)
    if len(newPoints)!= 0:
        for i in newPoints:
            myPoints.append(i)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints)
    cv2.imshow("Screen",stackImages(0.5,([img,imgRes])))
    cv2.waitKey(1)

    # print("x: {}\ty: {}\tRGB:{}".format(x, y, colors))

    if mouse.is_pressed('left'):
        draw = True
    elif mouse.is_pressed('right'):
        draw = False

    if cv2.waitKey(1) and kb.is_pressed('q'):
        cv2.destroyAllWindows()
        break
