from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from entity import Entity
from controller import Controller

if TYPE_CHECKING:
    from world import World


class Actor(Entity, ABC):
    controller: Controller

    def __init__(self, controller: Controller, position, state):
        super().__init__(position, state)
        self.controller = controller

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
