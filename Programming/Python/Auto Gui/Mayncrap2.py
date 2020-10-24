#Mayncrap sell
import pyautogui as pg
import time

commandsell = '/essentials:sell hand'
commandbuy = '/buy'
pg.FAILSAFE = True
pg.PAUSE = 1
pg.hotkey('alt','tab')
time.sleep(3)
pg.hotkey('t')

pg.write(commandbuy)
pg.moveTo(887,446)
pg.click()
pg.moveTo(891,361)
pg.click()
pg.moveTo(1067,441)
pg.PAUSE = 0.5
for i in range(0,36):
	pg.click()
pg.PAUSE = 1
for i in range(0,3):
	pg.press('esc')

pg.press('t')
pg.write(commandsell)

