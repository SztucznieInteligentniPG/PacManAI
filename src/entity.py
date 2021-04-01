from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from position import Position

if TYPE_CHECKING:
    from world import World

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
    def destroy(self, world: World):  # usunięcie siebie ze świata
        pass

    @abstractmethod
    def model(self):  # zwraca informację jak narysować
        #  TODO dodać zwracany typ, nwm co potrzebuje renderer
        pass

