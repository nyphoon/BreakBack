import pygame
import res
import cal
from arrow import Arrow
from game_map import GameMap

pygame.init()

gameDisplay = pygame.display.set_mode( res.size_display )
pygame.display.set_caption( res.text_caption )
pygame.display.set_icon( res.surface_icon )
clock = pygame.time.Clock()

game_map = GameMap(res.position_game_map, res.size_game_map, res.color_map,
					 res.size_grid, res.game_map_grids, 
					 res.width_game_map_wall, res.color_wall)
arrow_p1 = Arrow(res.size_grid, (50,50), (1,0), 3, res.color_p1)
arrow_p2 = Arrow(res.size_grid, (50,50), (0,1), 1, res.color_p2)

# register key done event
key_control = { res.control_p1['right']:lambda :arrow_p1.set_direction((1,0)),
				res.control_p1['left']:	lambda :arrow_p1.set_direction((-1,0)),
				res.control_p1['up']:	lambda :arrow_p1.set_direction((0,-1)),
				res.control_p1['down']:	lambda :arrow_p1.set_direction((0,1)),
				res.control_p2['right']:lambda :arrow_p2.set_direction((1,0)),
				res.control_p2['left']:	lambda :arrow_p2.set_direction((-1,0)),
				res.control_p2['up']:	lambda :arrow_p2.set_direction((0,-1)),
				res.control_p2['down']:	lambda :arrow_p2.set_direction((0,1))
				}

def game_encounter():
	# arrow encounter detect and handle
	if( cal.distance(arrow_p1.position, arrow_p2.position) < res.distance_collision):
		# pygame.draw.rect(gameDisplay, res.color_obj, [0,0,30,30], 5)
		if(arrow_p1.direction == arrow_p2.direction):
			return res.game_brokeback
		elif(arrow_p1.direction == cal.reverse(arrow_p2.direction)):
			arrow_p1.set_direction( cal.reverse(arrow_p1.direction) )
			arrow_p1.position = (arrow_p1.position[0]+arrow_p1.direction[0]*res.distance_collision, 	
								arrow_p1.position[1]+arrow_p1.direction[1]*res.distance_collision)
			arrow_p2.set_direction( cal.reverse(arrow_p2.direction) )
			arrow_p2.position = (arrow_p2.position[0] + arrow_p2.direction[0]*res.distance_collision,
								arrow_p2.position[1] + arrow_p2.direction[1]*res.distance_collision)
			return res.game_collision
		else:
			return res.game_sidemiss

def game_loop():
	game_exit = False
	while not game_exit:
		# handle event
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True

			if event.type == pygame.KEYDOWN:
				for key in key_control:
					if key == event.key:
						key_control[key]()
			# print(event)

		# progress game
		if (game_encounter() == res.game_brokeback):
			game_exit = True
		arrow_p1.progress()
		arrow_p2.progress()

		# render
		gameDisplay.fill(res.color_background)
		game_map.draw( gameDisplay )
		arrow_p1.draw( gameDisplay )
		arrow_p2.draw( gameDisplay )

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()