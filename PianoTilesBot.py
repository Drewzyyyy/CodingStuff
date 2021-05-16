import pyautogui as pg
import keyboard as kb
import win32api,win32con
import time

black=[1,1,1]

w=[697,700]
a=[771,700]
s=[873,700]
d=[955,700]

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def startBot():
    while not kb.is_pressed(','):
        # x,y=pg.position()
        # color = pg.pixel(x,y)
        # print("Color: {}".format(color))
        if pg.pixel(697,560)[0]==1:
            click(697,560)
        if pg.pixel(771,560)[0]==1:
            click(771,560)
        if pg.pixel(873,560)[0]==1:
            click(873,560)
        if pg.pixel(955,560)[0]==1:
            click(955,560)

while True:
    if kb.is_pressed('.'):
        startBot()


