import pygame

from enum import Enum


class Texture(Enum):
    WALL = pygame.image.load('img/wall.png')
    POINT = pygame.image.load('img/point.png')
    POWER_UP = pygame.image.load('img/powerup.png')
    PACMAN_0 = pygame.image.load('img/pacman1.png')
    PACMAN_1 = pygame.image.load('img/pacman2.png')
    PACMAN_2 = pygame.image.load('img/pacman3.png')
    ENEMY = pygame.image.load('img/enemy.png')
    ENEMY_FEARFUL = pygame.image.load('img/enemy_fearful.png')
    BLOCKADE = pygame.image.load('img/blockade.png')
