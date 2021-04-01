import pygame

from model import Model
from direction import Direction


class Renderer:
    texture_dic = {
        "PACMAN": [pygame.image.load('img/pacman1.png'),
                   pygame.image.load('img/pacman2.png'),
                   pygame.image.load('img/pacman3.png'),
                   ]
    }

    def __init__(self):
        pass

    def render(self, model: Model, display: pygame.display, frame):
        x = model.position.x
        y = model.position.y
        ox = model.offset.x
        oy = model.offset.y
        startX = 76
        startY = 76
        offset = 16

        texture = self.texture_dic[model.texture.name][frame]
        direction = model.direction
        if direction is Direction.UP:
            texture = pygame.transform.rotate(texture, 90)
        elif direction == Direction.DOWN:
            texture = pygame.transform.rotate(texture, -90)
        elif direction == Direction.LEFT:
            texture = pygame.transform.flip(texture, False, True)
        position = (startX + x*32 - ox*offset, startY + y*32 - oy*offset)
        display.blit(texture, position)
