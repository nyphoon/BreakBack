import pygame
import res
import cal

class KitBase( object ):
	def __init__(self, sur_icon):
		self.sur_icon = sur_icon
		self.sur_icon = pygame.transform.scale( self.sur_icon, res.size_kit)
	def invoke(self):
		raise NotImplementedError("Subclasses should implement this!")

class KitSpeedUp( KitBase ):
	def __init__(self):
		super().__init__(res.surface_icon_speedup)
	def invoke(self, arrow):
		arrow.set_speed( arrow.speed + 1 )

class KitReverse( KitBase ):
	def __init__(self):
		super().__init__(res.name_icon_reverse)
	def invoke(self, arrow):
		arrow.set_direction( cal.reverse(arrow.direction) )