from abc import ABC, abstractmethod
from model import Model
from world import World
from world_position import WorldPosition


class Entity(ABC):
    worldPosition: WorldPosition

    def __init__(self, worldPosition: WorldPosition):
        self.worldPosition = worldPosition

    @abstractmethod
    def serialize(self) -> int:
        pass

    def destroy(self, world: World):  # usunięcie siebie ze świata
        world.removeEntity(self.worldPosition)

    @abstractmethod
    def model(self) -> Model:  # zwraca informację jak narysować
        #  TODO dodać zwracany typ, nwm co potrzebuje renderer
        pass
