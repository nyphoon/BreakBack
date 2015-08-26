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
arrow_p1 = Arrow(res.size_arrow, game_map.grid_center((0,0)), (1,0), 3, res.color_p1)
arrow_p2 = Arrow(res.size_arrow, game_map.grid_center((23,0)), (-1,0), 1, res.color_p2)

# register key done event
key_control = { res.control_p1['right']:lambda :game_map_turn_correct(arrow_p1, game_map, (1,0)),
				res.control_p1['left']:	lambda :game_map_turn_correct(arrow_p1, game_map, (-1,0)),
				res.control_p1['up']:	lambda :game_map_turn_correct(arrow_p1, game_map, (0,-1)),
				res.control_p1['down']:	lambda :game_map_turn_correct(arrow_p1, game_map, (0,1)),
				res.control_p2['right']:lambda :game_map_turn_correct(arrow_p2, game_map, (1,0)),
				res.control_p2['left']:	lambda :game_map_turn_correct(arrow_p2, game_map, (-1,0)),
				res.control_p2['up']:	lambda :game_map_turn_correct(arrow_p2, game_map, (0,-1)),
				res.control_p2['down']:	lambda :game_map_turn_correct(arrow_p2, game_map, (0,1))
				}

def game_map_turn_correct( arrow, game_map, direction ):
	arrow.set_direction(direction)

def game_map_dump_correct( arrow, game_map ):
	# Is arrow near grid center that need to check current grid bound
	arrow_grid = game_map.detect_grid( arrow.position )
	grid_position = game_map.grid_center( arrow_grid )
	if ( cal.distance(arrow.position, grid_position) < res.distance_grid_wall_detect ):
		# convert vector to wall definition
		arrow_bump_wall = 0
		if (arrow.direction[0] == 0):
			if (arrow.direction[1] > 0):
				arrow_bump_wall = 1
			else:
				arrow_bump_wall = 4
		elif (arrow.direction[0] > 0):
			arrow_bump_wall = 2
		else:
			arrow_bump_wall = 8

		# arrow dumps wall
		if ( arrow_bump_wall & 
			game_map.grids[arrow_grid[1]*game_map.map_size[0]+arrow_grid[0]]  != 0 ):
			arrow.set_position( grid_position )


def game_arrow_encounter():
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
		if (game_arrow_encounter() == res.game_brokeback):
			game_exit = True

		arrow_p1.progress()
		game_map_dump_correct( arrow_p1, game_map )

		arrow_p2.progress()
		game_map_dump_correct( arrow_p2, game_map )

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