import pygame
import direction as Direction
import texture as Texture
from position import Position


class Model:
    direction: Direction
    texture: Texture
    position: Position
    offset: float

    def __init__(self, direction, texture, position, offset):
        self.direction = direction
        self.texture = texture
        self.pos = position
        self.off = offset

