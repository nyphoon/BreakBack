import pygame
import res
import arrow

pygame.init()

gameDisplay = pygame.display.set_mode( res.display_size )
pygame.display.set_caption( res.text_caption )
pygame.display.set_icon( res.surface_icon )
clock = pygame.time.Clock()

def game_loop():
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			# print(event)

		gameDisplay.fill( res.color_background )
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()