import pygame

from direction import Direction
from entity import Entity
from game_state import GameState
from model import Model
from world import World

BACKGROUND = (0, 0, 0)


class Renderer:
    display: pygame.display
    fontTitle: pygame.font
    font: pygame.font
    heartTexture: pygame.image

    def __init__(self, display: pygame.display):
        self.display = display
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.font_title = pygame.font.Font(pygame.font.get_default_font(), 40)
        self.heart_texture = pygame.image.load('img/heart.png')

    def renderModel(self, model: Model):
        x = model.position.x
        y = model.position.y
        ox = model.offset.x
        oy = model.offset.y
        startX = 30
        startY = 80
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

    def renderInfo(self, world:World):
        title = self.font_title.render('PACMAN', False, (252, 186, 3))
        self.display.blit(title, (240, 20))
        startX = 40
        startY = 20
        for i in range(world.lives):
            position = (startX + 40 * i, startY)
            self.display.blit(self.heart_texture, position)
        points = self.font.render('Punkty:  ' + str(int(world.score)), False, (255, 255, 255))
        self.display.blit(points, (500, 30))




    def render(self, world: World):
        self.display.fill(BACKGROUND)
        if world.gameState is GameState.WON:
            end = self.font_title.render('YOU WON', False, (252, 186, 3))
            self.display.blit(end, (240, 350))
        elif world.gameState is GameState.LOST:
            end = self.font_title.render('YOU LOST', False, (252, 186, 3))
            self.display.blit(end, (240, 350))
        else:
            self.renderInfo(world)
            for row in world.grid:
                for list in row:
                    for entity in list:
                        if isinstance(entity, Entity):
                            model = entity.model()
                            self.renderModel(model)
        pygame.display.update()
