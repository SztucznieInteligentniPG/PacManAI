from actor import Actor
from direction import Direction
from entity import Entity
from entity_dictionary import EntityDictionary
from model import Model
from position import Position
from texture import Texture
from wall import Wall
from world import World
from world_position import WorldPosition


class Player(Actor):
    direction: Direction
    speed: float = 1.0

    def __init__(self, controller, direction: Direction):
        super().__init__(controller)
        self.direction = direction

    def serialize(self) -> int:
        if self.direction == Direction.RIGHT:
            return EntityDictionary.PLAYER_RIGHT.value
        if self.direction == Direction.UP:
            return EntityDictionary.PLAYER_UP.value
        if self.direction == Direction.LEFT:
            return EntityDictionary.PLAYER_LEFT.value
        if self.direction == Direction.DOWN:
            return EntityDictionary.PLAYER_DOWN.value

    def update(self, world: World, deltaTime: float):
        self.controller.update(world)

        if self.direction is Direction.LEFT and self.controller.direction is Direction.RIGHT:
            self.direction = Direction.RIGHT
        elif self.direction is Direction.RIGHT and self.controller.direction is Direction.LEFT:
            self.direction = Direction.LEFT
        elif self.direction is Direction.UP and self.controller.direction is Direction.DOWN:
            self.direction = Direction.DOWN
        elif self.direction is Direction.DOWN and self.controller.direction is Direction.UP:
            self.direction = Direction.UP

        distance: float = self.speed * deltaTime

        destination: WorldPosition = world.getPositionInDirection(self.worldPosition, self.direction)
        entity: Entity = world.getEntity(destination)

        if destination == self.worldPosition or isinstance(entity, Wall):
            self.direction = self.controller.direction
            destination = world.getPositionInDirection(self.worldPosition, self.direction)
            entity = world.getEntity(destination)

        if destination != self.worldPosition and not isinstance(entity, Wall):
            distanceToDestination: float = self.getDistanceTo(destination)

            if distance >= distanceToDestination:
                distance -= distanceToDestination
                world.moveEntity(self, destination)
                self.direction = self.controller.direction
            else:
                self.moveInDirection(self.direction, distance)
                distance = 0

        destination = world.getPositionInDirection(self.worldPosition, self.direction)
        entity = world.getEntity(destination)

        if destination != self.worldPosition and not isinstance(entity, Wall):
            self.moveInDirection(self.direction, distance)

    def getDistanceTo(self, worldPosition: WorldPosition) -> float:
        return abs(self.position.x - worldPosition.x) + abs(self.position.y - worldPosition.y)

    def moveInDirection(self, direction: Direction, distance: float):
        if direction is Direction.UP:
            self.position.y -= distance
        elif direction is Direction.DOWN:
            self.position.y += distance
        elif direction is Direction.RIGHT:
            self.position.x += distance
        elif direction is Direction.LEFT:
            self.position.x -= distance

    def model(self) -> Model:
        return Model(self.direction, Texture.PACMAN_0, self.position, Position(0.5, 0.5))
