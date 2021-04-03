from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from controller import Controller
from entity import Entity
from vector2 import Vector2Int, Vector2Float

if TYPE_CHECKING:
    from world import World


class Actor(Entity, ABC):
    controller: Controller
    position: Vector2Float = None

    def __init__(self, controller: Controller):
        super().__init__()
        self.controller = controller

    def destroy(self, world: World):
        world.removeActor(self)

    def setPosition(self, worldPosition: Vector2Int):
        self.worldPosition = worldPosition
        self.position = Vector2Float(worldPosition.x, worldPosition.y)

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
