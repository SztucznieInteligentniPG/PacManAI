import pygame

from direction import Direction
from entity import Entity
from model import Model
from world import World

BACKGROUND = (0, 0, 0)


class Renderer:
    display: pygame.display

    def __init__(self, display: pygame.display):
        self.display = display

    def renderModel(self, model: Model):
        x = model.position.x
        y = model.position.y
        ox = model.offset.x
        oy = model.offset.y
        startX = 76
        startY = 76
        offset = 16

        texture = model.texture.value
        direction = model.direction

        if direction is Direction.UP:
            texture = pygame.transform.rotate(texture, 90)
        elif direction == Direction.DOWN:
            texture = pygame.transform.rotate(texture, -90)
        elif direction == Direction.LEFT:
            texture = pygame.transform.flip(texture, True, False)

        position = (startX + x*32 - ox*offset, startY + y*32 - oy*offset)
        self.display.blit(texture, position)

    def render(self, world: World):
        self.display.fill(BACKGROUND)
        for row in world.grid:
            for entity in row:
                if isinstance(entity, Entity):
                    model = entity.model()
                    self.renderModel(model)
        pygame.display.update()
