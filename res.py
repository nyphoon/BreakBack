import pygame
import os

import cal

dir_res = 'res'
name_icon = 'brokeback.png'
name_start = 'start.png'
name_icon_speedup = 'kit_speedup.png'
name_icon_reverse = 'kit_reverse.png'
text_caption = 'Broke Back'

tick_game = 60

fontsize_msg = 32

width_game_map_wall = 4

size_display = (1280, 720)
size_game_map = (960, 720)
size_panel_p1 = (150, 720)
size_panel_p2 = (150, 720)
size_grid = (60, 60) # 16x12 (960/60,720/60) grids will be created
size_arrow = (size_grid[0]-2*width_game_map_wall, size_grid[1]-2*width_game_map_wall)
size_kit = ( size_grid[0]-5*width_game_map_wall, size_grid[1]-5*width_game_map_wall )

grid_position_start_p1 = (0,0)
grid_position_start_p2 = (15, 0)

position_game_map = (160, 0)
position_panel_p1 = (0, 0)
position_panel_p2 = (size_display[0]-150, 0)

game_map_grids = (	12,	5,	5,	4,	5,	5,	4,	5,	5,	4,	5,	5,	4,	5,	5,	6,
					10,	12,	5,	2,	15,	15,	10,	12,	6,	10,	15,	15,	8,	5,	6,	10,
					10,	10,	15,	10,	15,	15,	10,	10,	10,	10,	15,	15,	10,	15,	10,	10,
					8,	2,	15,	8,	5,	4,	1,	3,	9,	1,	4,	5,	2,	15,	8,	2,
					10,	10,	15,	10,	15,	10,	12,	4,	4,	6,	10,	15,	10,	15,	10,	10,
					10,	9,	5,	2,	15,	8,	0,	0,	0,	0,	2,	15,	8,	5,	3,	10,
					10,	12,	5,	2,	15,	8,	0,	0,	0,	0,	2,	15,	8,	5,	6,	10,
					10,	10,	15,	10,	15,	10,	9,	1,	1,	3,	10,	15,	10,	15,	10,	10,
					8,	2,	15,	8,	5,	1,	4,	6,	12,	4,	1,	5,	2,	15,	8,	2,
					10,	10,	15,	10,	15,	15,	10,	10,	10,	10,	15,	15,	10,	15,	10,	10,
					10,	9,	5,	2,	15,	15,	10,	9,	3,	10,	15,	15,	8,	5,	3,	10,
					9,	5,	5,	1,	5,	5,	1,	5,	5,	1,	5,	5,	1,	5,	5,	3)

game_map_grids_blank=(	12,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	4,	6,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						8,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,
						9,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1, 3)

speed_max = 10

distance_collision = size_grid[0]/2
# speed should not bigger than this, or arrow will escape
distance_grid_wall_detect = speed_max
distance_grid_turn = size_grid[0]/4

color_background = (30, 30, 30)
color_msg = (222,222,222)
color_obj = (123, 123, 222)
color_p1 = (100, 100, 250)
color_p2 = (250, 100, 100)
color_map = (10, 10, 10)
color_wall = (100, 250, 100)


unit_len = 1
def unit(num):
	return unit_len * num

# Configuration of generating kit in game_map
kit_freq = tick_game*3
kit_max = 7

# enum game event
game_brokeback = 1
game_collision = 2
game_sidemiss = 3


# pygame var
surface_icon = pygame.image.load( os.path.join(dir_res, name_icon) )
surface_icon_speedup = pygame.image.load( os.path.join(dir_res, name_icon_speedup) )
surface_icon_reverse = pygame.image.load( os.path.join(dir_res, name_icon_reverse) )

# p1 and p2 's panel size is the same. use same local layout
slot_layout = ( (size_panel_p1[0]/3,100,50,50), (size_panel_p1[0]/3,200,50,50), (size_panel_p1[0]/3,300,50,50) )
control_p1 = { 'left':pygame.K_a, 'right':pygame.K_d, 'up':pygame.K_w, 'down':pygame.K_s, 'kit':pygame.K_LSHIFT}
control_p2 = { 'left':pygame.K_LEFT, 'right':pygame.K_RIGHT, 'up':pygame.K_UP, 'down':pygame.K_DOWN, 'kit':pygame.K_RSHIFT}
