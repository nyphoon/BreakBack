import pygame

display_size = (800, 600)

text_caption = 'Broke Back'

path_icon = './res/brokeback.png'
surface_icon = pygame.image.load( path_icon )
# surface_icon = pygame.suface

control_p1 = {}
control_p2 = {}

color_background = (30, 30, 30)
color_obj = (222, 222, 222)

unit_len = 1
def unit(num):
	return unit_len * num