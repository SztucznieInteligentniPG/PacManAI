from actor import Actor
from blockade import Blockade
from direction import Direction
from enemy import Enemy
from entity_dictionary import EntityDictionary
from game_state import GameState
from model import Model
from point import Point
from power_up import PowerUp
from reward import Reward
from texture import Texture
from vector2 import Vector2Int, Vector2Float
from wall import Wall
from world import World


class Player(Actor):
    direction: Direction
    speed: int = 3
    isSleeping: bool = False
    tickTimer: int = 0

    def __init__(self, controller, direction: Direction):
        super().__init__(controller)
        self.direction = direction
        self.collisionBox = Vector2Float(1, 1)

    def setPosition(self, worldPosition: Vector2Int):
        super().setPosition(worldPosition)
        if self.spawn is None:
            self.spawn = worldPosition

    def serialize(self) -> int:
        if self.direction == Direction.RIGHT:
            return EntityDictionary.PLAYER_RIGHT.value
        if self.direction == Direction.UP:
            return EntityDictionary.PLAYER_UP.value
        if self.direction == Direction.LEFT:
            return EntityDictionary.PLAYER_LEFT.value
        if self.direction == Direction.DOWN:
            return EntityDictionary.PLAYER_DOWN.value

    def update(self, world: World, tickRate: int):
        self.tickTimer += 1

        destination = world.getPositionInDirection(self.worldPosition, self.direction)

        if self.tickTimer >= tickRate / self.tickRate():
            if not self.isSleeping:
                colliding = self.checkCollidingEntities(world)

                for entity in colliding:
                    if isinstance(entity, Point) or isinstance(entity, PowerUp):
                        entity.collect(world)
                    if isinstance(entity, Enemy) and world.gameState is GameState.PSYCHODELIC:
                        world.addScore(Reward.KILLED_GHOST)
                        entity.die(world)

                distance = self.speed / self.tickRate()

                if destination != self.worldPosition and self.isWalkable(world, destination):
                    distanceToDestination: float = self.getDistanceTo(destination)
                    if distance >= distanceToDestination:
                        distance -= distanceToDestination
                        world.moveEntity(self, destination)
                        if self.controller.direction is not None:
                            destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
                            if self.isWalkable(world, destination):
                                self.direction = self.controller.direction

                destination = world.getPositionInDirection(self.worldPosition, self.direction)

                if destination != self.worldPosition and self.isWalkable(world, destination):
                    self.moveInDirection(self.direction, distance)

                self.controller.update(world)

                if self.controller.direction is not None and (
                    destination == self.worldPosition or
                    not self.isWalkable(world, destination)
                ):
                    destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
                    if self.isWalkable(world, destination):
                        self.direction = self.controller.direction

            self.tickTimer = 0
        else:
            if not self.isSleeping and destination != self.worldPosition and self.isWalkable(world, destination):
                self.moveModelInDirection(self.direction, self.speed / tickRate)

    def isWalkable(self, world: World, position: Vector2Int) -> bool:
        if world.hasEntityOfType(position, Blockade) or world.hasEntityOfType(position, Wall):
            return False
        return True

    def die(self, world: World):
        world.getKilled(self)

    def respawn(self, world: World):
        self.direction = Direction.RIGHT
        world.putActor(self, self.spawn)
        self.isSleeping = True

    def wakeUp(self):
        self.isSleeping = False

    def model(self) -> Model:
        return Model(self.direction, Texture.PACMAN_0, self.modelPosition, Vector2Float(0.5, 0.5))

    def tickRate(self) -> int:
        return self.speed * 2
