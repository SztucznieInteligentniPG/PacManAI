from direction import Direction
from texture import Texture
from vector2 import Vector2Float


class Model:
    direction: Direction
    texture: Texture
    position: Vector2Float
    offset: Vector2Float

    def __init__(self, direction: Direction, texture: Texture, position: Vector2Float, offset: Vector2Float):
        self.direction = direction
        self.texture = texture
        self.position = position
        self.offset = offset
