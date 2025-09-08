import pygame
import sys
import os
import argparse

from OTTO.pet import *
from OTTO.Helper import *
from OTTO.Player import *
from OTTO.Dialog import *

"""
    TODO 1 : Add command line arguement(DONE) , for first opening and transparent background
    TODO 2 : Add platform check for linux , macos and windows (DONE)
    TODO 3 : Added dialogs and storyline
"""


def FirstTimeRun(screen, bgcolor, sSize):
    font = load_font("Fonts/Regular.ttf", 16)
    # text = font.render('OTTER', False, (255 , 255 , 255))

    # Load spritesheet (with rows: idle, run, jump)
    spritesheet = Spritesheet("oldhero.png")
    player = Player(200, 0, spritesheet, frame_width=128,
                    frame_height=128, ssize=sSize, scale=3)
    all_sprites = pygame.sprite.Group(player)

    dialog_lines = [
        "Hear now the words carried on starlight,",
        "from the shining towers of Talajai, the empire of crystal spires and boundless science…",

        "I, the Emperor of Talajai, master of the engines of the cosmos and keeper of the radiant crown,",
        "send forth a gift most rare to you, noble Princess of Mahur.",

        "Not machines of steel, nor treasures of circuitry,",
        "but a living companion, woven from both light and ancient code,",
        "a faithful creature known as Shishimanu."

        "Shishimanu shall wander with you through the enchanted valleys of your realm of screen,",
        "amid the forests, rivers, and mountains of Mahur,",
        "bringing laughter to your halls and comfort to your heart.",

        "And on this day, when the constellations themselves bend in honor of your birth,",
        "I proclaim with joy:",

        "Happy Birthday, Princess of Mahur! "
        "May your path be ever bright, your heart ever joyful,",
        "and may the bond between the science of Talajai and the magic of Mahur...",
        "shine eternal across the stars and the mountains alike.",
        "✨ Thus is it spoken, thus is it bestowed. ✨"
    ]

    dialog = Dialog(dialog_lines, font, pygame.Rect(50, 200, 500, 100))

    clock = pygame.time.Clock()
    running = True
    # Main loop
    while running:
        dt = clock.tick(60)
        screen.fill(bgcolor)  # fully transparent background
        # screen.blit(text , (400 , 400))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("LEFT CLICK")
                if event.button == 2:
                    print("MIDDLE CLICK")
                if event.button == 3:
                    print("RIGHT CLICK")

        all_sprites.update(keys, dt / 1000)
        all_sprites.draw(screen)

        # Handle dialog input
        dialog.handle_input(keys)

        # Draw dialog
        dialog.draw(screen)

        if dialog.active == False:
            return

        pygame.display.flip()


def run_game():
    # command line arguements
    parser = argparse.ArgumentParser(description="Run the OTTO virtual pet")
    parser.add_argument("--HBD", action="store_true",
                        help="for first time running the script")
    parser.add_argument("--t", type=int, default=1,
                        help="Choose whether the BG is transparent or not (0 => let the program choose ; 1 => black ; 2 => transparent)")
    parser.add_argument("--speed", type=int, default=100,
                        help="Movement speed of the pet")
    parser.add_argument("--fullscreen", action="store_true",
                        help="Run in fullscreen mode")
    parser.add_argument("--wsize", type=int, default=800,
                        help="Enter the size of the window (default = 800) ")
    parser.add_argument("--wpos", type=int, default=800,
                        help="Enter the position of the window on the screen (default =(800 , 800)) ")
    args = parser.parse_args()

    platform = sys.platform

    if args.t == 2 and platform != "win32":
        print(
            "[Error] : Your Platform does not support transparent backgrounds for windows.")
        pygame.quit()
        sys.exit()
        return

    DEFAULT_WIDTH = DEFAULT_HEIGHT = args.wsize
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (args.wpos, args.wpos)
    # Initialize
    pygame.init()
    # Window settings
    if args.fullscreen:
        screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)  # fullscreen
    else:
        screen = pygame.display.set_mode(
            (DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.NOFRAME)  # no border
    pygame.display.set_caption("VP")

    WIDTH, HEIGHT = screen.get_size()
    BGCOLOR = (255, 0, 128)  # Transparency color

    if args.t == 0:
        if platform == "win32":
            import win32api
            import win32con
            import win32gui
            # Create layered window
            hwnd = pygame.display.get_wm_info()["window"]
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                                   win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
            # Set window transparency color
            win32gui.SetLayeredWindowAttributes(
                hwnd, win32api.RGB(*BGCOLOR), 0, win32con.LWA_COLORKEY)
        else:
            BG = (0, 0, 0)
        print("Default")

    elif args.t == 1:
        BGCOLOR = (0, 0, 0)
        print("Black")

    elif args.t == 2:
        # Create layered window
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        # Set window transparency color
        win32gui.SetLayeredWindowAttributes(
            hwnd, win32api.RGB(*BGCOLOR), 0, win32con.LWA_COLORKEY)
        print("Transparent BG")

    vPet = Pet(WIDTH // 2, HEIGHT // 2)

    if args.HBD:
        FirstTimeRun(screen, BGCOLOR, (WIDTH, HEIGHT))
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
                    # pyright: ignore[reportAttributeAccessIssue]
                    vPet.target_pos = (
                        pos[0] - vPet.size[0] // 2, pos[1] - vPet.size[1] // 2)
                    vPet.animations.set_state("Moving")

        vPet.Update(dt)
        vPet.Draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
    sys.exit()
