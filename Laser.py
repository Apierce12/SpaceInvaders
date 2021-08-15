import pygame
import random
from pygame.locals import *

class Laser(pygame.sprite.Sprite):
    def __init__(self): 
        super(Laser, self).__init__()
        self.surf = pygame.Surface([4, 20])
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
 
    def update(self):
        self.rect.y -= 10

        if self.rect.y < 0:
            self.kill()