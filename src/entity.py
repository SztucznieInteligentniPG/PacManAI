from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from model import Model
from vector2 import Vector2Int

if TYPE_CHECKING:
    from world import World


class Entity(ABC):
    worldPosition: Vector2Int = None

    def destroy(self, world: World):
        """
        Usuwa siebie z grida świata

        :param world: świat z którego usuwany jest entity
        :return:
        """
        world.removeEntity(self)

    def setPosition(self, worldPosition: Vector2Int):
        self.worldPosition = worldPosition

    @abstractmethod
    def serialize(self) -> int:
        pass

    @abstractmethod
    def model(self) -> Model:
        """
        Tworzy Model opisujący jak narysować Entity w obecnym momencie

        :return: Model danego Entity
        """
        pass
