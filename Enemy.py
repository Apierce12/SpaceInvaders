import pygame
import random
from pygame.locals import *;

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/ufo.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(random.randint(0, 1500), 0))
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.move_ip(0, 1)
        if self.rect.bottom > 800:
            self.kill()