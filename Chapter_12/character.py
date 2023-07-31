import pygame

class Dog():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/dog.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)


        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.centerx -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= 1
        
        # Update rect object from self.center - might need to be changed now to handle
        # movement in two directions properly.
        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx


    def blitme(self):
        self.screen.blit(self.image, self.rect)
