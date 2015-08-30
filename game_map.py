import pygame
import kit
import random

def direction_to_wall(direction):
	if (direction[0] == 0):
		if (direction[1] > 0):
			# down
			return 1
		else:
			# up
			return 4
	elif (direction[0] > 0):
		# right
		return 2
	else:
		# left
		return 8

class KitInMap(object):
	def __init__(self, kit, grid_position):
		self.kit = kit
		self.grid_position = grid_position

class GameMap(object):
	def __init__(self, position, size, color_bk, grid_size, grids, width_wall, color_wall):
		self.position = position
		self.size = size
		self.color = color_bk
		self.grid_size = grid_size
		self.grids = grids
		self.color_wall = color_wall
		self.width_wall = width_wall
		self.map_size = ( int(size[0]/grid_size[0]), int(size[1]/grid_size[1]) ) # X*Y grids in this map

	def grid_position(self, map_position):
		return ( self.position[0] + int(map_position[0]*self.grid_size[0]),
		 self.position[1] + int(map_position[1]*self.grid_size[1]) )

	def grid_center(self, map_position):
		return ( self.position[0] + int((map_position[0]+0.5)*self.grid_size[0]),
		 self.position[1] + int((map_position[1]+0.5)*self.grid_size[1]) ) 

	def detect_grid(self, position):
		return (int((position[0]-self.position[0])/self.grid_size[0]),
		 int((position[1]-self.position[1])/self.grid_size[1])) 
 
	# Kits Contorl
	def kit_reset(self, kit_max, kit_freq):
		self.kit_roster = [kit.KitSpeedUp, kit.KitReverse] # defined here currently. may be a argument if necessary
		self.kit_max = kit_max
		self.kit_freq = kit_freq
		self.kit_freq_count = 0
		self.kit_list = []

	def kit_gen(self):
		# cannot generate kit in a closed grid
		map_position = (random.randint(0, self.map_size[0]-1), random.randint(0, self.map_size[1]-1))
		while ( self.grids[ map_position[0]+map_position[1]*self.map_size[0] ] == 15 ):
			map_position = (random.randint(0, self.map_size[0]-1), random.randint(0, self.map_size[1]-1))

		self.kit_list.append( KitInMap( random.choice(self.kit_roster)(), map_position ) )

	def kit_progress(self):
		if ( len(self.kit_list) < self.kit_max and self.kit_freq_count == self.kit_freq ):
			self.kit_gen()
			self.kit_freq_count = 0
		else:
			self.kit_freq_count = self.kit_freq_count + 1

	# Drawing
	def draw_kit(self, sur):
		for kitinmap in self.kit_list:
			grid_center = self.grid_center(kitinmap.grid_position)
			sur.blit( kitinmap.kit.sur_icon, (grid_center[0]-kitinmap.kit.size_icon[0]/2, grid_center[1]-kitinmap.kit.size_icon[1]/2) )

	def draw_grid(self, sur, grid_position, grid_size, grid):
		### graw wall
		# down side 0001
		if (grid & 1 == 1):
			pygame.draw.rect(sur, self.color_wall, 
				(grid_position[0], grid_position[1]+grid_size[1]-self.width_wall, self.grid_size[0], self.width_wall))
		# right side 0010
		if (grid & 2 == 2):
			pygame.draw.rect(sur, self.color_wall, 
				(grid_position[0]+grid_size[0]-self.width_wall, grid_position[1], self.width_wall, self.grid_size[1]))
		# up side 0100
		if (grid & 4 == 4):
			pygame.draw.rect(sur, self.color_wall, 
				(grid_position[0], grid_position[1], self.grid_size[0], self.width_wall))
		# left side 1000
		if (grid & 8 == 8):
			pygame.draw.rect(sur, self.color_wall, 
				(grid_position[0], grid_position[1], self.width_wall, self.grid_size[1]))

	def draw(self, sur):
		pygame.draw.rect( sur, self.color, self.position+self.size)
		for i in range(len(self.grids)):
			# grid center for debugging
			# pygame.draw.circle(sur, self.color_wall, self.grid_center( (int(i%self.map_size[0]), int(i/self.map_size[0])) ), 2) 
			self.draw_grid(sur, 
				( int(i%self.map_size[0])*self.grid_size[0]+self.position[0], int(i/self.map_size[0])*self.grid_size[1]+self.position[1] ), 
				self.grid_size, 
				 self.grids[i])
		self.draw_kit( sur )
