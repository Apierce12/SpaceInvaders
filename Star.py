import pygame
import random
from pygame.locals import *;

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.surf = pygame.image.load("images/star.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(center=(random.randint(0, 1500),0))

    def update(self):
        self.rect.move_ip(0, 0)
        if self.rect.bottom > 800:
            self.kill()