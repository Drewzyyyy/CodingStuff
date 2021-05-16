import cv2
import keyboard as kb
import numpy as np

neutral_face = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
vid = cv2.VideoCapture(0)
vid.set(3,640) #width
vid.set(4,480) #height
vid.set(10,100) #Brightness

while True:
    success, img = vid.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = neutral_face.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,"Person",(x+(w//2)-10,(y+(h//2)-10)),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,150,0),3) #(Source, Text, Origin, Font, Scale, Color, Thickness)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & kb.is_pressed('q'):
        break