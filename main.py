import pyautogui

from time import sleep


startx = 1659
starty = 1003
endx = 1691
endy = 1025

def get_image():
    return pyautogui.screenshot(region=(startx, starty, endx, endy))


while True:
    pixs = get_image().getpixel((1, 1))
    if pixs[0] == 0 and pixs[1] == 230 and pixs[2] == 203:
        pyautogui.click(startx, starty)
        pyautogui.moveRel(0, -25)
    sleep(3)
    