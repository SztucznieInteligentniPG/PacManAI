from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from entity import Entity
from controller import Controller
from position import Position

if TYPE_CHECKING:
    from world import World


class Actor(Entity, ABC):
    controller: Controller
    position: Position

    def __init__(self, worldPosition, position: Position, controller: Controller):
        super().__init__(worldPosition)
        self.controller = controller
        self.position = position

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
