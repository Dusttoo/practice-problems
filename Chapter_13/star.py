import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen):
        super(Star, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)