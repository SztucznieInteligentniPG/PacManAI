from abc import ABC
from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from texture import Texture
from vector2 import Vector2Float


class Blockade(Entity, ABC):
    isClosed: bool

    def __init__(self):
        super().__init__()
        self.isClosed = True
        self.collisionBox = Vector2Float(0.5, 0.5)      # stoi w drzwiach tylko

    def serialize(self) -> int:
        return EntityDictionary.BLOCKADE.value

    def model(self) -> Model:
        return Model(
            Direction.DEFAULT,
            Texture.BLOCKADE,
            Vector2Float(self.worldPosition.x, self.worldPosition.y),
            Vector2Float(0.5, 0.5),
        )

    def setIsClosed(self, action):
        self.isClosed = action
