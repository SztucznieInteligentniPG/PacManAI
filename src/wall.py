from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from position import Position
from texture import Texture


class Wall(Entity):
    def serialize(self) -> int:
        return EntityDictionary.WALL

    def model(self) -> Model:
        return Model(
            Direction.DEFAULT,
            Texture.WALL,
            Position(self.worldPosition.x, self.worldPosition.y),
            Position(0.5, 0.5),
        )
