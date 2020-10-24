import pyautogui as pg
import keyboard
x, y = pg.position()

while True:
    
    pg.moveTo(x,y)
    if keyboard.is_pressed('up'): y -= 20
    if keyboard.is_pressed('down'): y += 20
    if keyboard.is_pressed('left'): x -= 20
    if keyboard.is_pressed('right'): x += 20

