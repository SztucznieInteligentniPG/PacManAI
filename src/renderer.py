import pygame

from direction import Direction
from model import Model
from world import World


class Renderer:

    def __init__(self):
        pass

    def renderModel(self, model: Model, display: pygame.display, frame:int):
        x = model.position.x
        y = model.position.y
        ox = model.offset.x
        oy = model.offset.y
        startX = 76
        startY = 76
        offset = 16

        texture =model.texture.value[frame]
        direction = model.direction
        if direction is Direction.UP:
            texture = pygame.transform.rotate(texture, 90)
        elif direction == Direction.DOWN:
            texture = pygame.transform.rotate(texture, -90)
        elif direction == Direction.LEFT:
            texture = pygame.transform.flip(texture, False, True)
        position = (startX + x*32 - ox*offset, startY + y*32 - oy*offset)
        display.blit(texture, position)

    def render(self, world: World, display: pygame.display, frame: int):
        for row in world.grid:
            for en in row:
                model = en.model()
                self.renderModel(model, display, frame)
