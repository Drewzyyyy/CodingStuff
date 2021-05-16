import cv2
# img_1 = cv2.imread("Images/Comrade_doggo.jpg")
#
# cv2.imshow("Output",img_1)
# cv2.waitKey(0)
vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,100)
while True:
    success, img = vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break