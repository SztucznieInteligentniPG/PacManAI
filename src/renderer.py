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
            texture = self.texture_dic[model.texture.name][frame]
            dir = model.direction
            if dir.value == Direction.UP.value:
                texture = pygame.transform.rotate(texture, 90)
            elif dir.value == Direction.DOWN.value:
                texture = pygame.transform.rotate(texture, -90)
            elif dir.value == Direction.LEFT.value:
                texture = pygame.transform.flip(texture, False, True)

            display.blit(texture, (x, y))
