import pyautogui as pg 
from selenium import webdriver

import time
pg.FAILSAFE = True

def pause():
    secsleep = 2
    time.sleep(secsleep)
#Move to browser
pg.moveTo(713,1059,1)
pause()
pg.click()

while True:
    pg.moveTo(1913,105)
    pause()
    pg.dragTo(1913,969,1, button='left')
    pg.click(1027,147)

    #Long Sleep
    time.sleep(15)
    print("Done")