from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from entity import Entity
from controller import Controller
from position import Position
from world_position import WorldPosition

if TYPE_CHECKING:
    from world import World


class Actor(Entity, ABC):
    controller: Controller
    position: Position = None

    def __init__(self, controller: Controller):
        super().__init__()
        self.controller = controller

    def setPosition(self, worldPosition: WorldPosition):
        self.worldPosition = worldPosition
        self.position = Position(worldPosition.x, worldPosition.y)

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
