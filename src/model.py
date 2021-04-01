import pygame
import direction as Direction
import texture as Texture
from position import Position


class Model:
    direction: Direction
    texture: Texture
    pos: Position
    off: float

    def __init__(self, direction, tex, pos, off):
        self.direction = direction
        self.texture = tex
        self.pos = pos
        self.off = off

