from actor import Actor
from blockade import Blockade
from direction import Direction
from entity_dictionary import EntityDictionary
from game_state import GameState
from model import Model
from texture import Texture
from vector2 import Vector2Int, Vector2Float
from wall import Wall
from world import World


class Enemy(Actor):
    direction: Direction
    modelDirection: Direction
    speed = 3.0
    spawn: Vector2Int = None
    is_fearful: bool

    def __init__(self, controller, direction: Direction):
        super().__init__(controller)
        self.direction = direction
        self.collisionBox = Vector2Float(1, 1)

        if direction is Direction.LEFT:
            self.modelDirection = Direction.LEFT
        else:
            self.modelDirection = Direction.RIGHT

    def setPosition(self, worldPosition: Vector2Int):
        super().setPosition(worldPosition)

        if self.spawn is None:
            self.spawn = worldPosition

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

        self.is_fearful = world.gameState is GameState.PSYCHODELIC

        self.controller.update(world)

        distance = self.speed * deltaTime

        colliding = self.checkCollidingEntities(world)

        destination = world.getPositionInDirection(self.worldPosition, self.direction)
        if self.controller.direction is not None and (
                destination == self.worldPosition or
                world.hasEntityOfType(destination, Wall) or
                world.hasBlockade(destination, self.position)
        ):
            destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
            if not world.hasEntityOfType(destination, Wall) and not world.hasBlockade(destination, self.position):
                self.direction = self.controller.direction

        if destination != self.worldPosition and not world.hasEntityOfType(destination, Wall) and \
                not world.hasBlockade(destination, self.position):
            distanceToDestination: float = self.getDistanceTo(destination)
            if distance >= distanceToDestination:
                distance -= distanceToDestination
                world.moveEntity(self, destination)
                if self.controller.direction is not None and not self.isOppositeDirection(self.controller.direction):
                    destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
                    if not world.hasEntityOfType(destination, Wall) and \
                            not world.hasBlockade(destination, self.position):
                        self.direction = self.controller.direction
            else:
                self.moveInDirection(self.direction, distance)
                distance = 0

        for entity in colliding:
            if isinstance(entity, Player) and world.gameState is not GameState.PSYCHODELIC:
                entity.die(world)

        destination = world.getPositionInDirection(self.worldPosition, self.direction)

        if destination != self.worldPosition and not world.hasEntityOfType(destination, Wall) and \
                not world.hasBlockade(destination, self.position):
            self.moveInDirection(self.direction, distance)

        if self.direction is not Direction.UP and self.direction is not Direction.DOWN:
            self.modelDirection = self.direction

    def isOppositeDirection(self, direction: Direction) -> bool:
        if self.direction is Direction.UP and direction is Direction.DOWN or \
                self.direction is Direction.DOWN and direction is Direction.UP or \
                self.direction is Direction.LEFT and direction is Direction.RIGHT or \
                self.direction is Direction.RIGHT and direction is Direction.LEFT:
            return True
        return False

    def die(self, world: World):
        world.moveEntity(self, self.spawn)

    def model(self) -> Model:
        return Model(self.modelDirection, Texture.ENEMY_FEARFUL if self.is_fearful else Texture.ENEMY, self.position,
                     Vector2Float(0.5, 0.5))
