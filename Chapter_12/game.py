import sys
import pygame
from character import Dog

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Practice Game")

    dog = Dog(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("blue")
        dog.blitme()
        pygame.display.flip()

run_game()