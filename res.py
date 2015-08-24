import pygame
import os

import cal

dir_res = 'res'
name_icon = 'brokeback.png'

size_display = (1280, 720)
size_game_map = (960, 720)
size_grid = (40, 40)

position_game_map = (160, 0)

game_map_wall = ()

distance_collision = size_grid[0]/2

text_caption = 'Broke Back'


color_background = (30, 30, 30)
color_obj = (123, 123, 222)
color_p1 = (100, 100, 250)
color_p2 = (250, 100, 100)
color_map = (10, 10, 10)
color_wall = (200, 200, 200)

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
