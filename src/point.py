from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from texture import Texture
from vector2 import Vector2Float
from world import World


class Point(Entity):
    def serialize(self) -> int:
        return EntityDictionary.POINT.value

    def model(self) -> Model:
        return Model(
            Direction.DEFAULT,
            Texture.POINT,
            Vector2Float(self.worldPosition.x, self.worldPosition.y),
            Vector2Float(0.5, 0.5),
        )

    def collect(self, world: World):
        self.destroy(world)
        world.addScore(1)
