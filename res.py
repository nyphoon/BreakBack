import pygame
import os

import cal

dir_res = 'res'
name_icon = 'brokeback.png'

text_caption = 'Broke Back'

width_game_map_wall = 4

size_display = (1280, 720)
size_game_map = (960, 720)
size_grid = (40, 40)
size_arrow = (size_grid[0]-2*width_game_map_wall, size_grid[1]-2*width_game_map_wall)

position_game_map = (160, 0)
# position_start_p1 =
# position_start_p2 =

game_map_grids = (12,	4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4, 6,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,15,1,2,4,8,12,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					8,	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 2,
					9,	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 3)

distance_collision = size_grid[0]/2
distance_grid_wall_detect = size_grid[0]/10
distance_grid_turn = size_grid[0]/4

color_background = (30, 30, 30)
color_obj = (123, 123, 222)
color_p1 = (100, 100, 250)
color_p2 = (250, 100, 100)
color_map = (10, 10, 10)
color_wall = (100, 250, 100)

unit_len = 1
def unit(num):
	return unit_len * num

# enum game event
game_brokeback = 1
game_collision = 2
game_sidemiss = 3


# pygame var
surface_icon = pygame.image.load( os.path.join(dir_res, name_icon) )

control_p1 = { 'left':pygame.K_a, 'right':pygame.K_d, 'up':pygame.K_w, 'down':pygame.K_s, 'kit':pygame.K_LSHIFT}
control_p2 = { 'left':pygame.K_LEFT, 'right':pygame.K_RIGHT, 'up':pygame.K_UP, 'down':pygame.K_DOWN, 'kit':pygame.K_RSHIFT}
