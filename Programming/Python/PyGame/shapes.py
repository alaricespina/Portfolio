import pygame as pg
#https://www.pg.org/docs/ref/draw.html
#rect,polygon,circle,ellipse,arc,line,lines,aaline,aalines
pg.init()
sw = 1000
sh = 300
screen = pg.display.set_mode((sw,sh))
ev = pg.event.get()
clock = pg.time.Clock()

class make():
	global sw
	global sh
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 10
		self.height = 10
		self.changespeed = 10 
		self.n = 1
		self.whilestep = 1

	def boxin(self,color):
		while self.x < sw and self.whilestep == 0:
			pg.draw.rect(screen, color, pg.Rect(self.x,self.y,self.width,self.height))
			pg.display.update()
			print("Changing at x" + str(self.x))
			self.x += self.changespeed

		if self.y + self.width >= sh:
			self.whilestep == 1
			if self.n == 1:
				print("done")
				self.n == 2

		elif self.x >= sw:
			self.whilestep = 0
			self.x = 0
			self.y += self.height
			print("reset")
	
	def snek(self,color,increment):
		pg.draw.rect(screen, color, pg.Rect(self.x+((self.whilestep-1)*2*self.width),self.y,sw,self.height))
		pg.draw.rect(screen, color, pg.Rect((sw-self.width),self.y,self.width,sh))
		pg.draw.rect(screen, color, pg.Rect(self.x,(sh-self.height),sw,self.height))
		pg.draw.rect(screen, color,	pg.Rect(self.x,(self.width+(self.whilestep*increment)),self.width,sh-self.width+increment))
		self.whilestep += 1


animate = make()
animate.n = 2
run = True
while run:
	for event in ev:
		if event.type == pg.QUIT:
			run = False

	animate.snek((255,0,255),10)

	
	pg.display.update()
	clock.tick(30)