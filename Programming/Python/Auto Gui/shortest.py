import pyautogui as pg
import time

link = "http://gestyy.com/eeAuyh"
pg.PAUSE = 2.5

pg.click(518,1066) #Explorer

for x in range(0,5):
    pg.click(221,52) #Address Bar
    pg.write(link)
    pg.press('enter')
    time.sleep(15)
    pg.click(1849,97)
    time.sleep(3)
    pg.click(470,17)
    