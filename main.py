import pygame
import res
from arrow import Arrow

pygame.init()

gameDisplay = pygame.display.set_mode( res.display_size )
pygame.display.set_caption( res.text_caption )
pygame.display.set_icon( res.surface_icon )
clock = pygame.time.Clock()

arrow = Arrow((100,100), (50,50), (1,0), 1, res.color_obj)

key_control = { res.control_p1['right']:lambda :arrow.set_direction((1,0)),
				res.control_p1['left']:	lambda :arrow.set_direction((-1,0)),
				res.control_p1['up']:	lambda :arrow.set_direction((0,-1)),
				res.control_p1['down']:	lambda :arrow.set_direction((0,1))
				}

def game_loop():
	game_exit = False
	while not game_exit:
		# handle event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
			# for key in 
			if event.type == pygame.KEYDOWN:
				for key in key_control:
					if key == event.key:
						key_control[key]()
			print(event)

		# progress game
		arrow.progress()

		# render
		gameDisplay.fill(res.color_background)
		arrow.draw( gameDisplay )

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()