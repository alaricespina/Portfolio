import pygame as pg
import math

pg.init()
sw, sh = 400, 600
black, white, blue, green, red = (0,0,0), (255,255,255), (0,0,255), (0,255,0), (255,0,0)
fw, fh, fx, fy, gw, gh, movspd = 300, 500, 50, 50, 100, 25, 0
ballx, bally, rad = (fw//2)+fx, (fh//2)+fy, 10
screen = pg.display.set_mode((sw,sh))
clock = pg.time.Clock()
run = True
movspdx ,movspdy = 0, 0
trix,triy,trirad,tria,trib = (fw//2)+fx, (fh//2)+fy, 20, math.radians(210), math.radians(330)

def slowdown(x):
	a = x
	if x > 0: a -= 1
	if x < 0: a += 1
	return a

while run:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

	screen.fill(black)
	#Playing Field
	pg.draw.rect(screen, white, pg.Rect(fx-10,fy-10,fw+20,fh+20)) #Outer Field
	pg.draw.rect(screen, green, pg.Rect(fx,fy,fw,fh)) #Inner Field
	pg.draw.rect(screen, blue, pg.Rect(fw//2,fy, gw, gh)) #Upper Goal
	pg.draw.rect(screen, blue, pg.Rect(fw//2, fh+25, gw, gh)) #Lower Goal

	if ballx >= fw//2 and ballx <= (fw//2)+gw and bally <= fy+gh or bally >= fh+25: print("Goal")

	#Ball
	pg.draw.circle(screen, red, (ballx,bally), rad)

	pressed = pg.key.get_pressed()

	
	if pressed[pg.K_UP] and bally >= fy+rad: movspdy, movspdx = -10, movspdx//2 #Up
	if pressed[pg.K_DOWN] and bally <= fy+fh-rad: movspdy, movspdx = 10, movspdx//2 #Down
	if pressed[pg.K_LEFT] and ballx >= fx+rad: movspdx, movspdy = -10, movspdy//2 #Left
	if pressed[pg.K_RIGHT] and ballx <= fx+fw-rad: movspdx, movspdy = 10, movspdy//2 #Right
	if pressed[pg.K_SPACE]: 
		bally, ballx, movspdx, movspdy = sh//2, sw//2, 0, 0 #Spacebar  
		print("reset")  

	ballx, bally = ballx+movspdx, bally+movspdy

	movspdx = slowdown(movspdx)
	movspdy = slowdown(movspdy)
		
	if bally <= fy+rad: bally = fy+rad
	if bally >= fy+fh-rad: bally = fy+fh-rad
	if ballx <= fx+rad: ballx = fx+rad
	if ballx >= fx+fw-rad: ballx = fx+fw-rad
	
	#here
	
	tricoords = [(trix,triy-trirad),(trix+(math.floor(math.cos(tria)*trirad)),triy-math.floor(math.sin(tria)*trirad)),(trix+math.floor(math.cos(trib)*trirad),triy-math.floor(math.sin(trib)*trirad))]
	pg.draw.polygon(screen, blue, tricoords)
	print(tricoords)

	pg.display.update()
	clock.tick(30)
