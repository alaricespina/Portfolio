import pyautogui as pg 
pg.FAILSAFE = True
pg.PAUSE = 1

pg.click(712,1062)
pg.click(939,313)
x = 939
y = 313
while True:
    pg.rightClick()