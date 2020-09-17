import pygame

pygame.init()
sw = 500
sh = 300
screen = pygame.display.set_mode((sw, sh))
x = sw/2
y = sh/2
dim = 10
white = (255,255,255)
black = (0,0,0)
movspd = dim/20
clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y >= 0: y -= movspd
        if pressed[pygame.K_DOWN] and y <= sh-(y-dim): y += movspd
        if pressed[pygame.K_LEFT] and x >= 0: x -= movspd
        if pressed[pygame.K_RIGHT]and x <= sw-dim: x += movspd
        
        screen.fill(black)
        pygame.draw.rect(screen,white,pygame.Rect(x,y, dim, dim))
        pygame.display.flip()
        clock.tick(60)
