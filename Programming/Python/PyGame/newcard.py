import pygame
import random
#Improved Card Game
pygame.init()

correct = 0
run = True
clock = pygame.time.Clock()
sw = 1200
sh = 600
screen = pygame.display.set_mode((sw,sh))

class make():
	coordssel = 0
	def __init__(self,n):
		global sw
		global sh
		make.not_sel = (255,255,0)
		make.sel = (0,255,255)
		make.chosen = (0,255,0)
		make.x = sw//9
		make.y = sh//9
		make.width = 150
		make.height = 300
		
		pygame.draw.rect(screen, make.not_sel, pygame.Rect(int(n*make.x), make.y, make.width, make.height))

	def check(self,n):
		mousepos = pygame.mouse.get_pos()
		(mx, my) = mousepos
		if mx >= (n*make.x) and my >= make.y and my <= (make.y+make.height) and mx <= ((n*make.x)+make.width):
			pygame.draw.rect(screen, make.sel, pygame.Rect(int(n*make.x), make.y, make.width, make.height))
			make.coordssel = n*make.x
	
	def ccard(self,n):
		global correct
		print("Selected Coords" + str(self.coordssel))
		print("Current Coords" + str(n*make.x))
		if self.coordssel == (n*make.x):
			correct += 1
		else:
			correct = 0
		print("Correct Score After Checking:" + str(correct))	
		a = 5
		while a >= 0:
			pygame.draw.rect(screen, make.chosen, pygame.Rect((n*make.x)-25, make.y-25, make.width+50, make.height+50))
			pygame.time.delay(100)
			pygame.display.update()
			pygame.draw.rect(screen, make.not_sel, pygame.Rect((n*make.x)-25, make.y-25, make.width+50, make.height+50))
			pygame.time.delay(100)
			pygame.display.update()
			pygame.draw.rect(screen, make.sel, pygame.Rect((n*make.x)-25, make.y-25, make.width+50, make.height+50))
			pygame.time.delay(100)
			pygame.display.update()
			a -= 1

		screen.fill((0, 0, 0))

class score():
	global sw
	global sh
	global correct
	green = (0,255,0)
	blue = (0,0,255)
	def __init__(self):
		font = pygame.font.Font('freesansbold.ttf', 32)
		text = font.render(str(correct), True, self.green, self.blue)
		textRect = text.get_rect()
		textRect.center = (sw // 2, int(sh*0.75))
		screen.blit(text, textRect)


while run:
	streak = score()

	card1 = make(1)
	card2 = make(3)
	card3 = make(5)
	card4 = make(7)

	card1.check(1)
	card2.check(3)
	card3.check(5)
	card4.check(7)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			p = random.randint(0,3)
			print(p)
			ch = [1,3,5,7]
			end = make(1)
			end.ccard(ch[p])
	pygame.display.update()
	clock.tick(60)

