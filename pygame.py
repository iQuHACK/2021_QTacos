import pygame, sys
pygame.init()

size = (1280,720)

screen = pygame.display.set_mode(size)

while True:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()

	