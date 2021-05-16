import cv2
import numpy as np
import keyboard as kb
import pyautogui
from WindowCapture import WindowCapture

wincap = WindowCapture('#announcements - Discord')

while True:

    screen = wincap.get_screenshot()

    cv2.imshow("Screen",screen)

    if cv2.waitKey(1) and kb.is_pressed('q'):
        cv2.destroyAllWindows()
        break