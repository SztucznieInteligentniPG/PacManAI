from abc import ABC, abstractmethod
from position import Position

class Entity(ABC):
    position: Position
    state: int  # stan danego elementu

    def __init__(self, position, state):
        self.position = position
        self.state = state

    @abstractmethod
    def serialize(self) -> int:
        pass

    @abstractmethod
    def destroy(self, world):  # usunięcie siebie ze świata
        from world import World
        pass

    @abstractmethod
    def model(self):  # zwraca informację jak narysować
        #  TODO dodać zwracany typ, nwm co potrzebuje renderer
        pass

