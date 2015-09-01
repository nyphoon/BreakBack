import pygame
import kit

class Arrow (object):
	def __init__(self, size, position, direction, speed, speed_max, color):
		self.size = size
		self.position = position;
		self.direction = direction

		self.color = color
		self.speed = speed
		self.speed_max = speed_max
		self.kits = []

	def bound_point(self):
		dirction_vert = (-self.direction[1], self.direction[0] )

		return ( ( self.position[0]+self.direction[0]*self.size[0]/2, self.position[1]+self.direction[1]*self.size[1]/2 ),
			( self.position[0]+(dirction_vert[0]-self.direction[0])*self.size[0]/2, self.position[1]+(dirction_vert[1]-self.direction[1])*self.size[1]/2 ),
			( self.position[0]-self.direction[0]*self.size[0]/2, self.position[1]-self.direction[1]*self.size[1]/2 ),
			( self.position[0]+(-dirction_vert[0]-self.direction[0])*self.size[0]/2, self.position[1]+(-dirction_vert[1]-self.direction[1])*self.size[1]/2 ) )

	def progress(self):
		self.position = (self.position[0]+self.direction[0]*self.speed, self.position[1]+self.direction[1]*self.speed)

	def draw(self, sur):
		pygame.draw.polygon(sur, self.color, self.bound_point())

	def set_speed(self, speed):
		if (speed <= self.speed_max):
			self.speed = speed
		
	def set_position(self, position):
		self.position = position

	def set_direction(self, direction):
		self.direction = direction

	# kit control
	def kit_save(self, kit):
		self.kits.append( kit )

	def kit_invoke(self):
		if self.kits:
			self.kits[0].invoke(self)
			self.kits = self.kits[1:]
