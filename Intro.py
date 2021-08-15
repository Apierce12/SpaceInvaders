import pygame
from pygame.locals import *


#create Explosion class
class Intro(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(0, 71):
			img = pygame.image.load(f"images/intro/frame_{num}_delay-0.02s.gif")
			img = pygame.transform.scale(img, (1500, 800))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.counter = 0

	def update(self):
		explosion_speed = 10
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.index = 0