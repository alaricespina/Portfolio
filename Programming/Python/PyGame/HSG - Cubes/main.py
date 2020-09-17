#Hypersimple Game, Cube focus
import pygame
pygame.init()

class Main():
	def __init__(self):		
		

		self.screenwidth = 500
		self.screenheight = 300
		self.screen = pygame.display.set_mode((self.screenwidth,self.screenheight))
		self.clock = pygame.time.Clock()

		a = Player(self.screen,self.screenwidth//2,self.screenheight//2, 100)

		#Game Itself
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					break

			pressed = pygame.key.get_pressed()

class Player():
	white = (255,255,255)
	def __init__(self, surface, x, y, dimension):
		self.screen = surface
		self.dimension = dimension
		pygame.draw.rect(self.screen,self.white,pygame.Rect(x, y, dimension, dimension))

class Enemy():
	def __init__(self, surface, x, y, dimension):
		pass



Game = Main()



