import pyautogui as pg
import time

pg.PAUSE = 1.5
n = 0
if pg.locateCenterOnScreen('Chrome Selected.png') == None:
	#Click on Chrome
	pg.click(pg.locateCenterOnScreen('Chrome Unselected.png'))

while n <= 10:
	pg.moveTo(1266,51,duration=1)
	pg.click(1266,51)
	time.sleep(3)
	pg.click(pg.locateCenterOnScreen('CopyIcon.png'))
	pg.click(720,130)
	pg.hotkey('ctrl','a')
	pg.hotkey('ctrl','v')
	pg.press('enter')

	waitforvid = True
	while waitforvid:
		if pg.locateCenterOnScreen('Red Outline.png') != None:
			pg.moveTo(1260,700)
			pg.moveTo(471,237,duration=1)
			pg.click(471,237)
			waitforvid = False
		if pg.locateCenterOnScreen('RankedLow.png') != None:
			pg.moveTo(1260,700)
			pg.moveTo(690,500,duration=1)
			pg.click(690,500)
			waitforvid = False

	pg.moveTo(1260,700)
	pg.moveTo(441,402,duration=1)
	pg.press('g')

	waitforfinish = True
	while waitforfinish:
		if pg.locateCenterOnScreen('Task Complete.png') != None:
			pg.moveTo(1260,700)
			pg.moveTo(690,500,duration=1)
			pg.click(690,500)
			waitforfinish = False

	print(n)
	n += 1
print("Done on 10 offers")