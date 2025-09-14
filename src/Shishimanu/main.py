import pygame
import sys
import os
import argparse

from Shishimanu.pet import *
from Shishimanu.Helper import *
from Shishimanu.Player import *
from Shishimanu.Dialog import *

"""
    TODO 1 : Add command line arguement(DONE) , for first opening and transparent background (DONE)
    TODO 2 : Add platform check for linux , macos and windows (DONE)
    TODO 3 : Added dialogs and storyline (DoONE)

    TODO 4 : Add various status like hunger , sleep , fun and health to the virtual pet
    TODO 5 : Make virtual pet move across screen randomly according to the statuses
    TODO 6 : Add various interactions with the virtual pet
"""


def FirstTimeRun(screen, bgcolor, sSize, font):
    # text = font.render('OTTER', False, (255 , 255 , 255))
    # Load spritesheet (with rows: idle, run, jump)
    spritesheet = Spritesheet("oldhero.png")
    player = Player(200, 0, spritesheet, frame_width=128,
                    frame_height=128, ssize=sSize, scale=2)
    all_sprites = pygame.sprite.Group(player) # pyright: ignore[reportArgumentType]

    dialog_lines = [
        "Hear now the words carried on starlight,",
        "from the shining towers of Talajai, the empire of crystal spires and boundless science…",

        "I, Tirthesh Mahajan, the Emperor of Talajai, master of the engines of the cosmos and keeper of the radiant crown,",
        "send forth a gift most rare to you, Pratiksha Kumbhar, the noble Princess of Mahur.",

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

    dialog = Dialog(dialog_lines, font, pygame.Rect(50, 200, 300, 130))
    bg_layer1 = load_image("background/background_layer_1.png")
    bg_layer1 = pygame.transform.scale(bg_layer1, sSize)

    # bg_layer2 = load_image("background/background_layer_2.png")
    # bg_layer2 = pygame.transform.scale(bg_layer2, sSize)

    bg_layer3 = load_image("background/background_layer_3.png")
    bg_layer3 = pygame.transform.scale(bg_layer3, sSize)

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

        screen.blit(bg_layer1, (0, 0))
        # screen.blit(bg_layer2, (0, 0))
        screen.blit(bg_layer3, (0, 0))

        all_sprites.update(keys, dt / 1000)
        all_sprites.draw(screen)

        # Handle dialog input
        dialog.handle_input(keys[pygame.K_SPACE])

        # Draw dialog
        dialog.draw(screen, (player.rect.x, player.rect.y))

        if dialog.active == False:
            return

        pygame.display.flip()


def run_game():
    # command line arguements
    parser = argparse.ArgumentParser(description="Run the Shishimanu virtual pet")
    parser.add_argument("--HBD", action="store_true",
                        help="for first time running the script")
    parser.add_argument("--t", type=int, default=0,
                        help="Choose whether the BG is transparent or not (0 => let the program choose ; 1 => black ; 2 => transparent)")
    parser.add_argument("--speed", type=int, default=100,
                        help="Movement speed of the pet")
    parser.add_argument("--fullscreen", action="store_true",
                        help="Run in fullscreen mode")
    parser.add_argument("--wsize", type=int, default=600,
                        help="Enter the size of the window (default = 800) ")
    parser.add_argument("--wpos", type=int, default=[100, 100], nargs=2, metavar=['X', 'Y'], # pyright: ignore[reportArgumentType]
                        help="Enter the position of the window on the screen (default = (100 , 100) ")
    args = parser.parse_args()

    platform = sys.platform

    if args.t == 2 and platform != "win32":
        print(
            "[Error] : Your Platform does not support transparent backgrounds for windows.")
        pygame.quit()
        sys.exit()
        return

    print("Use WAD keys for movement")  
    print("And press SPACE to see next dialog")
    iiii = input("enter 55 to continue: ")

    DEFAULT_WIDTH = DEFAULT_HEIGHT = args.wsize
    # Initialize
    pygame.init()
    # Window settings
    if args.fullscreen:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
            args.wpos[0], args.wpos[1])
        screen = pygame.display.set_mode(
            (DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.NOFRAME)  # no border
    else:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, -20)
        display_info = pygame.display.Info()
        desktop_size = (display_info.current_w, display_info.current_h)
        screen = pygame.display.set_mode(
            desktop_size, pygame.NOFRAME)  # fullscreen
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
            BGCOLOR = (0, 0, 0)
        print("Default")

    elif args.t == 1:
        BGCOLOR = (0, 0, 0)
        print("Black")

    elif args.t == 2:
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
        print("Transparent BG")

    font = load_font("Fonts/Bold.ttf", 16)
    vPet = Pet(WIDTH // 2, HEIGHT // 2, font)

    if args.HBD:
        FirstTimeRun(screen, BGCOLOR, (WIDTH, HEIGHT), font)
    clock = pygame.time.Clock()
    running = True
    # Main loop
    while running:
        dt = clock.tick(60)
        screen.fill(BGCOLOR)  # fully transparent background

        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if vPet.Check_Mouse_Click(mouse_pos):
                        vPet.animations.set_state("Spin")

                if event.button == 3:
                    tarpos = (mouse_pos[0] - vPet.size[0] //
                              2, mouse_pos[1] - vPet.size[1] // 2)
                    vPet.target_pos = tarpos[:]
                    vPet.animations.set_state("Moving")

        vPet.Update(dt)
        vPet.Draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
