from enum import Enum

import pygame


class Texture(Enum):
    PACMAN_0 = pygame.image.load('img/pacman1.png')
    PACMAN_1 = pygame.image.load('img/pacman2.png')
    PACMAN_2 = pygame.image.load('img/pacman3.png')

