from enum import Enum

import pygame


class Texture(Enum):
    PACMAN = [pygame.image.load('img/pacman1.png'),
               pygame.image.load('img/pacman2.png'),
               pygame.image.load('img/pacman3.png'),
               ]
