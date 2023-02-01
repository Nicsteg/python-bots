from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con


# tile 1 position Point(x=-1529, y=350) (183, 187, 235)
# tile 2 position Point(x=-1477, y=348) (0, 0, 0)
# tile 3 position Point(x=-1407, y=341) (175, 178, 234)
# tile 4 position Point(x=-1270, y=346) (179, 182, 234)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # uses left click
    time.sleep(.005)  # pauses mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # uses left click


while not keyboard.is_pressed("q"):
    # checks if the RED(R) value is 0 which is black
    # [0] = R, [1] = G, [2] = B for pixel color
    if pyautogui.pixel(-1557, 350)[0] == 0:
        click(-1557, 350)
    if pyautogui.pixel(-1464, 350)[0] == 0:
        click(-1464, 350)
    if pyautogui.pixel(-1377, 350)[0] == 0:
        click(-1377, 350)
    if pyautogui.pixel(-1285, 350)[0] == 0:
        click(-1285, 350)



