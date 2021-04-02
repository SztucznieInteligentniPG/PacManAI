from direction import Direction
from position import Position
from texture import Texture


class Model:
    direction: Direction
    texture: Texture
    position: Position
    offset: Position

    def __init__(self, direction: Direction, texture: Texture, position: Position, offset: Position):
        self.direction = direction
        self.texture = texture
        self.position = position
        self.offset = offset
