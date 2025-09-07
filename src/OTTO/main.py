import pygame
import sys
import win32api
import win32con
import win32gui

from OTTO.pet import *
from OTTO.Helper import *

""" 
    TODO 1 : Add command line arguement , for first opening and transparent background
    TODO 2 : Add platform check for linux , macos and windows
    TODO 3 : Added dialogs and storyline 
"""

# Initialize
pygame.init()

# Window settings
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)  # no border
pygame.display.set_caption("Virtual Pet")
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


vPet = Pet(WIDTH // 2, HEIGHT // 2)


def run_game():
    clock = pygame.time.Clock()
    running = True
    # Main loop
    while running:
        dt = clock.tick(60)
        screen.fill(fuchsia)  # fully transparent background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    vPet.target_pos = (pos[0] - vPet.size[0] // 2 , pos[1] - vPet.size[1] // 2)  # pyright: ignore[reportAttributeAccessIssue]
                    vPet.animations.set_state("Moving")

        vPet.Update(dt)
        vPet.Draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
