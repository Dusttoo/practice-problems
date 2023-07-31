import sys
import pygame
from pygame.sprite import Group
from raindrop import Raindrop


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Raindrops")
    raindrops = Group()

    raindrop = Raindrop(screen)
    available_space_x = 800 - 2 * raindrop.rect.width
    number_raindrops_x = int(available_space_x / (2 * raindrop.rect.width))

    for raindrop_number in range(number_raindrops_x):
        raindrop = Raindrop(screen)
        raindrop_width = raindrop.rect.width
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrops.add(raindrop)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill("white")
        raindrops.draw(screen)
        raindrops.update()
        pygame.display.flip()


run_game()
