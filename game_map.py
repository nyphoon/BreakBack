import pygame
import res

class GameMap(object):
	def __init__(self, position, size, grid_size, grid, color_wall=res.color_wall, color_bk=res.color_map):
		self.position = position
		self.size = size
		self.grid_size = grid_size
		self.grid = grid
		self.color_wall = color_wall
		self.color = color_bk

	def draw(self, sur):
		pygame.draw.rect( sur, self.color, self.position+self.size)