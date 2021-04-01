from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from position import Position
from texture import Texture
from world_position import WorldPosition


class Wall(Entity):
    def __init__(self, worldPosition: WorldPosition):
        super().__init__(self, worldPosition)

    def serialize(self) -> int:
        return EntityDictionary.WALL

    def model(self) -> Model:  # zwraca informację jak narysować
        return Model(
            Direction.RIGHT,
            Texture.PACMAN,
            Position(self.worldPosition.x, self.worldPosition.y),
            Position(0.5, 0.5),
        )