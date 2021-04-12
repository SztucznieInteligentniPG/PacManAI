from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from texture import Texture
from vector2 import Vector2Float


class Wall(Entity):
    def __init__(self):
        self.collisionBox = Vector2Float(1,1)

    def serialize(self) -> int:
        return EntityDictionary.WALL.value

    def model(self) -> Model:
        return Model(
            Direction.DEFAULT,
            Texture.WALL,
            Vector2Float(self.worldPosition.x, self.worldPosition.y),
            Vector2Float(0.5, 0.5),
        )
