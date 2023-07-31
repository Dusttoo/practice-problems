import sys
import pygame
from pygame.sprite import Group
from star import Star

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Stars")
    stars = Group()
    
    star = Star(screen)
    available_space_x = 800 - 2 * star.rect.width
    available_space_y = 800 - (3 * star.rect.height)
    number_stars_x = int(available_space_x / (2 * star.rect.width))
    number_rows =  int(available_space_y / (2 * star.rect.height))

    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            star = Star(screen)
            star_width = star.rect.width
            star.x = star_width + 2 * star_width * star_number
            star.rect.x = star.x
            star.rect.y = star.rect.height + 2 * star.rect.height * row_number
            stars.add(star)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill("white")
        # star.blitme()
        stars.draw(screen)
        pygame.display.flip()

run_game()

