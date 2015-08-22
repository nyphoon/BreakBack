import pygame
import os

dir_res = 'res'
name_icon = 'brokeback.png'

display_size = (800, 600)

text_caption = 'Broke Back'



color_background = (30, 30, 30)
color_obj = (222, 222, 222)

unit_len = 1
def unit(num):
	return unit_len * num

# pygame var
surface_icon = pygame.image.load( os.path.join(dir_res, name_icon) )

# control_p1 = {left:, right:, up:, down:, kit:}
control_p2 = {}
