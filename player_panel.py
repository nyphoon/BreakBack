import pygame

class PowerBar(object):
	def __init__(self, rect, max, color, color_bk):
		self.rect = rect
		self.max = max
		self.color = color
		self.color_bk = color_bk
	def set_power(self, power):
		self.power = power
	def draw(self, surface):
		pygame.draw.rect( surface, self.color_bk, self.rect)
		pygame.draw.rect( surface, self.color, 
				( self.rect[0], self.rect[1]+int(self.rect[3]*(self.max-self.power)/self.max), self.rect[2], int(self.rect[3]*self.power/self.max) )
				)
	
class PlayerPanel(object):
	def __init__(self, position, size, color_bk):
		self.position = position
		self.size = size
		self.color = color_bk
		self.item_max = 0

	def set_player(self, arrow):
		self.arrow = arrow
	
	def set_power_bar(self, power_bar):
		self.power_bar = power_bar
	
	def set_item_slot(self, slot_list):
		self.item_max = len( slot_list )
		self.slot_list = [(slot[0]+self.position[0], slot[1]+self.position[1], slot[2], slot[3]) for slot in slot_list]
		
	# Drawing
	def draw(self, sur):
		# background
		pygame.draw.rect( sur, self.color, self.position+self.size)
		
		# display speed of arrow
		self.power_bar.set_power( self.arrow.speed )
		self.power_bar.draw( sur )
		
		# display kit of arrow
		i = 0
		n = len(self.arrow.kits)
		for slot in self.slot_list:
			pygame.draw.rect( sur, (0,0,0), slot) # slot back ground
			if ( i != n ):
				sur_icon = self.arrow.kits[i].sur_icon
				sur.blit( sur_icon, slot)
				i += 1
				