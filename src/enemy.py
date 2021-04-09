from actor import Actor
from direction import Direction
from entity_dictionary import EntityDictionary
from model import Model
from texture import Texture
from vector2 import Vector2Int, Vector2Float
from wall import Wall
from world import World


class Enemy(Actor):
    direction: Direction
    speed = 1.0

    def __init__(self, controller, direction: Direction):
        super().__init__(controller)
        self.direction = direction

    def serialize(self) -> int:
        if self.direction == Direction.RIGHT:
            return EntityDictionary.ENEMY_RIGHT.value
        if self.direction == Direction.UP:
            return EntityDictionary.ENEMY_UP.value
        if self.direction == Direction.LEFT:
            return EntityDictionary.ENEMY_LEFT.value
        if self.direction == Direction.DOWN:
            return EntityDictionary.ENEMY_DOWN.value

    def update(self, world: World, deltaTime: float):
        from player import Player

        self.controller.update(world)

        distance = self.speed * deltaTime

        destination = world.getPositionInDirection(self.worldPosition, self.direction)
        if self.controller.direction is not None and (
                destination == self.worldPosition or
                world.hasEntityOfType(destination, Wall)
        ) and not self.isOppositeDirection(self.controller.direction):
            destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
            if not world.hasEntityOfType(destination, Wall):
                self.direction = self.controller.direction

        if destination != self.worldPosition and not world.hasEntityOfType(destination, Wall):
            distanceToDestination: float = self.getDistanceTo(destination)
            if distance >= distanceToDestination:
                distance -= distanceToDestination
                world.moveEntity(self, destination)
                if self.controller.direction is not None and not self.isOppositeDirection(self.controller.direction):
                    destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
                    if not world.hasEntityOfType(destination, Wall):
                        self.direction = self.controller.direction
            else:
                self.moveInDirection(self.direction, distance)
                distance = 0

        # placeholder dopóki nie będzie kolizji
        if world.hasEntityOfType(self.worldPosition, Player):
            for entity in world.getEntities(self.worldPosition):
                if isinstance(entity, Player):
                    entity.kill()

        destination = world.getPositionInDirection(self.worldPosition, self.direction)

        if destination != self.worldPosition and not world.hasEntityOfType(destination, Wall):
            self.moveInDirection(self.direction, distance)

    def isOppositeDirection(self, direction: Direction) -> bool:
        if self.direction is Direction.UP and direction is Direction.DOWN or \
                self.direction is Direction.DOWN and direction is Direction.UP or \
                self.direction is Direction.LEFT and direction is Direction.RIGHT or \
                self.direction is Direction.RIGHT and direction is Direction.LEFT:
            return True
        return False

    def model(self) -> Model:
        return Model(self.direction, Texture.PACMAN_0, self.position, Vector2Float(0.5, 0.5))
