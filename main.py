import pygame
import res
from arrow import Arrow

pygame.init()

gameDisplay = pygame.display.set_mode( res.display_size )
pygame.display.set_caption( res.text_caption )
pygame.display.set_icon( res.surface_icon )
clock = pygame.time.Clock()

arrow = Arrow((10,10), (50,50), (1,0), 1, res.color_obj)

def game_loop():
	game_exit = False
	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
			print(event)

		gameDisplay.fill(res.color_background)
		arrow.draw( gameDisplay )
		arrow.progress()

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()