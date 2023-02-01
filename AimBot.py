from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

time.sleep(3)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # uses left click
    # time.sleep(.05)  # pauses mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  # uses left click


while not keyboard.is_pressed("q"):
    pic = pyautogui.screenshot(region=(170, 308, 625, 500))
    width, height = pic.size
    # color of center of target = (255, 219, 195)
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            # stored red value in r green value in g and blue value in b
            r, g, b = pic.getpixel((x, y))
            if b == 195:
                click(x+170, y+308)
                time.sleep(0.1)
                break


