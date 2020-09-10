from pyautogui import pixelMatchesColor, click
from time import sleep

while True:
    if pixelMatchesColor(1691, 1025, (0, 202, 177), 29):
        click(1691, 1025)
    sleep(3)