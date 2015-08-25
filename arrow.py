import pygame
import kit

class Arrow (object):
	def __init__(self, size, position, direction, speed, color):
		self.size = size
		self.position = position;
		self.direction = direction

		self.color = color
		self.speed = speed
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

	def set_direction(self, direction):
		self.direction = direction