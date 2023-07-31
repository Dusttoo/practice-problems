import pygame
import random
from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self, screen):
        super(Raindrop, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def update(self):
        self.y += random.randint(1, 3)
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
