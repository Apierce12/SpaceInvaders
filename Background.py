import pygame
from pygame.locals import *

#create background class
class Background(pygame.sprite.Sprite):
	def __init__(self):
		super(Background, self).__init__()
		self.images = []
		for num in range(1, 128):
			img = pygame.image.load(f"images/space_files/spaceFrame{num}.gif")
			img = pygame.transform.scale(img, (1500, 800))
			img = pygame.transform.rotate(img, 180)
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.counter = 0

	def update(self):
		movement_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= movement_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		if self.index >= len(self.images) - 1 and self.counter >= movement_speed:
			self.index = 0