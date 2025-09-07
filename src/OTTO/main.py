import pygame
import sys

from OTTO.pet import *
from OTTO.Helper import *

# Initialize
pygame.init()

# Window settings
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)  # no border
pygame.display.set_caption("Virtual Pet")

vPet = Pet(WIDTH // 2, HEIGHT // 2)


def run_game():
    clock = pygame.time.Clock()
    running = True
    # Main loop
    while running:
        dt = clock.tick(60)
        screen.fill((0, 0, 0, 0))  # fully transparent background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    vPet.target_pos = (pos[0] - vPet.size[0] // 2 , pos[1] - vPet.size[1] // 2)
                    vPet.animations.set_state("Moving")

        vPet.Update(dt)
        vPet.Draw(screen)

        pygame.display.update()

    pygame.quit()
    sys.exit()
