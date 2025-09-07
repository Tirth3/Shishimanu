import pygame
import sys
import os
import win32api
import win32con
import win32gui
import argparse

from OTTO.pet import *
from OTTO.Helper import *
from OTTO.Player import *

""" 
    TODO 1 : Add command line arguement(DONE) , for first opening and transparent background 
    TODO 2 : Add platform check for linux , macos and windows (DONE)
    TODO 3 : Added dialogs and storyline 
"""

def FirstTimeRun(screen , bgcolor):
    font = load_font("Fonts/font1.ttf", 32)
    # text = font.render('OTTER', False, (255 , 255 , 255))

    player = Player(400 , 400)
    
    clock = pygame.time.Clock()
    running = True
    # Main loop
    while running:
        dt = clock.tick(60)
        screen.fill(bgcolor)  # fully transparent background
        # screen.blit(text , (400 , 400))
        player.dir = 0
        player.state = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_LEFT:
                    player.dir = -1
                    player.state = 1
                elif event.key == pygame.K_RIGHT:
                    player.dir = 1
                    player.state = 1
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("LEFT CLICK")
                if event.button == 2:
                    print("MIDDLE CLICK")
                if event.button == 3:
                    print("RIGHT CLICK")

        player.Update(dt)
        player.Draw(screen)
        pygame.display.flip()


def run_game():
    # command line arguements
    parser = argparse.ArgumentParser(description="Run the OTTO virtual pet")
    parser.add_argument("--HBD" , action="store_true" , help="for first time running the script")
    parser.add_argument("--t" , type=int , default=1 , help="Choose whether the BG is transparent or not (0 => let the program choose ; 1 => black ; 2 => transparent)")
    parser.add_argument("--speed", type=int, default=100, help="Movement speed of the pet")
    parser.add_argument("--fullscreen", action="store_true", help="Run in fullscreen mode")
    args = parser.parse_args()
    
    platform = sys.platform

    if args.t == 2 and platform != "win32":
        print("[Error] : Your Platform does not support transparent backgrounds for windows.")
        pygame.quit()
        sys.exit()
        return

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1000 , 300)
    # Initialize
    pygame.init()
    # Window settings
    if args.fullscreen:
        screen = pygame.display.set_mode((0 , 0), pygame.FULLSCREEN)  # fullscreen
    else:
        screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.NOFRAME)  # no border
    pygame.display.set_caption("VP")


    WIDTH, HEIGHT = screen.get_size()
    BGCOLOR = (255, 0, 128)  # Transparency color

    if args.t == 0:
        if platform == "win32":
            # Create layered window
            hwnd = pygame.display.get_wm_info()["window"]
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                                win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
            # Set window transparency color
            win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*BGCOLOR), 0, win32con.LWA_COLORKEY)
        else:
            BG = (0, 0 ,0)
        print("Default")

    elif args.t == 1:
        BGCOLOR = (0 , 0 , 0)
        print("Black")
    
    elif args.t == 2:
        # Create layered window
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                            win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        # Set window transparency color
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*BGCOLOR), 0, win32con.LWA_COLORKEY)
        print("Transparent BG")

    vPet = Pet(WIDTH // 2, HEIGHT // 2)

    if args.HBD:
        FirstTimeRun(screen , BGCOLOR)
    clock = pygame.time.Clock()
    running = True
    # Main loop
    while running:
        dt = clock.tick(60)
        screen.fill(BGCOLOR)  # fully transparent background

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
