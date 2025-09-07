import math
import pygame
import importlib.resources


def load_image(name):
    with importlib.resources.path("OTTO.assets", name) as path:
        return pygame.image.load(path)

def load_font(name , size):
    with importlib.resources.path("OTTO.assets", name) as path:
        return pygame.font.Font(path, size)


DEFAULT_WIDTH, DEFAULT_HEIGHT = 800, 800

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


def Distance(v1, v2):
    return math.sqrt(math.pow((v1[0] - v2[0]), 2) + math.pow((v1[1] - v2[1]), 2))
