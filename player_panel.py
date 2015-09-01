import pygame

class PlayerPanel(object):
	def __init__(self, position, size, color_bk):
		self.position = position
		self.size = size
		self.color = color_bk
		self.item_max = 0
	def set_player(self, arrow):
		self.arrow = arrow
	
	def set_item_slot(self, slot_list):
		self.item_max = len( slot_list )
		self.slot_list = [(slot[0]+self.position[0], slot[1]+self.position[1], slot[2], slot[3]) for slot in slot_list]
		
	# Drawing
	def draw(self, sur):
		pygame.draw.rect( sur, self.color, self.position+self.size)
		i = 0
		n = len(self.arrow.kits)
		for slot in self.slot_list:
			pygame.draw.rect( sur, (0,0,0), slot) # slot back ground
			if ( i != n ):
				sur_icon = self.arrow.kits[i].sur_icon
				sur.blit( sur_icon, slot)
				i += 1
				