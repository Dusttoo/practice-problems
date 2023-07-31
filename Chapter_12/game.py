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
            elif event.type == pygame.KEYDOWN:
                """Responds to keypresses"""
                if event.key == pygame.K_RIGHT:
                    dog.moving_right = True
                elif event.key == pygame.K_LEFT:
                    dog.moving_left = True
                elif event.key == pygame.K_DOWN:
                    dog.moving_down = True
                elif event.key == pygame.K_UP:
                    dog.moving_up = True
            elif event.type == pygame.KEYUP:
                """Responds to key releases"""
                if event.key == pygame.K_RIGHT:
                    dog.moving_right = False
                elif event.key == pygame.K_LEFT:
                    dog.moving_left = False
                elif event.key == pygame.K_DOWN:
                    dog.moving_down = False
                elif event.key == pygame.K_UP:
                    dog.moving_up = False


        dog.update()
        screen.fill("blue")
        dog.blitme()
        pygame.display.flip()

run_game()