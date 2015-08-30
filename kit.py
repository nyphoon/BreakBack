import pygame
import res
import cal

class KitBase( object ):
	def __init__(self, sur_icon, size_icon):
		self.sur_icon = sur_icon
		self.sur_icon = pygame.transform.scale( self.sur_icon, size_icon)
		self.size_icon = size_icon
	def invoke(self):
		raise NotImplementedError("Subclasses should implement this!")

class KitSpeedUp( KitBase ):
	def __init__(self):
		super().__init__(res.surface_icon_speedup, res.size_kit)
	def invoke(self, arrow):
		arrow.set_speed( arrow.speed + 1 )

class KitReverse( KitBase ):
	def __init__(self):
		super().__init__(res.surface_icon_reverse, res.size_kit)
	def invoke(self, arrow):
		arrow.set_direction( cal.reverse(arrow.direction) )