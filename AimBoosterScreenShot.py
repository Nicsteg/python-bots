import pyautogui

# left, top, width, height
iml = pyautogui.screenshot(region=(170, 308, 625, 500))
iml.save(r"C:\Users\nicks\PycharmProjects\BotProject\savedimage.png")