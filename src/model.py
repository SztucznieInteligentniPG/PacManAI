from direction import Direction
from texture import Texture
from position import Position


class Model:
    direction: Direction
    texture: Texture
    position: Position
    offset: Position

    def __init__(self, direction, texture, position, offset):
        self.direction = direction
        self.texture = texture
        self.position = position
        self.offset = offset

