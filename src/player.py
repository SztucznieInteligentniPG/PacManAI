from actor import Actor
from direction import Direction
from enemy import Enemy
from entity_dictionary import EntityDictionary
from model import Model
from point import Point
from power_up import PowerUp
from texture import Texture
from vector2 import Vector2Int, Vector2Float
from wall import Wall
from world import World


class Player(Actor):
    direction: Direction
    speed = 3.0
    spawn: Vector2Int = None

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

    def update(self, world: World, deltaTime: float):
        self.controller.update(world)

        # Zawracanie nie będac w środku grida może wywołać zatrzymanie się postaci
        # i inne dziwne rzeczy więc wyączam puki co tą możliwość

        # if self.direction is Direction.LEFT and self.controller.direction is Direction.RIGHT:
        #     self.direction = Direction.RIGHT
        # elif self.direction is Direction.RIGHT and self.controller.direction is Direction.LEFT:
        #     self.direction = Direction.LEFT
        # elif self.direction is Direction.UP and self.controller.direction is Direction.DOWN:
        #     self.direction = Direction.DOWN
        # elif self.direction is Direction.DOWN and self.controller.direction is Direction.UP:
        #     self.direction = Direction.UP

        distance = self.speed * deltaTime

        colliding = self.checkCollidingEntities(world)

        destination = world.getPositionInDirection(self.worldPosition, self.direction)
        if self.controller.direction is not None and (
            destination == self.worldPosition or
            world.hasEntityOfType(destination, Wall)
        ):
            destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
            if not world.hasEntityOfType(destination, Wall):
                self.direction = self.controller.direction

        if destination != self.worldPosition and not world.hasEntityOfType(destination, Wall):
            distanceToDestination: float = self.getDistanceTo(destination)
            if distance >= distanceToDestination:
                distance -= distanceToDestination
                world.moveEntity(self, destination)
                if self.controller.direction is not None:
                    destination = world.getPositionInDirection(self.worldPosition, self.controller.direction)
                    if not world.hasEntityOfType(destination, Wall):
                        self.direction = self.controller.direction
            else:
                self.moveInDirection(self.direction, distance)
                distance = 0

        for entity in colliding:
            if isinstance(entity, Point):
                entity.collect(world)
            if isinstance(entity, PowerUp):
                entity.collect(world)

        destination = world.getPositionInDirection(self.worldPosition, self.direction)

        if destination != self.worldPosition and not world.hasEntityOfType(destination, Wall):
            self.moveInDirection(self.direction, distance)

    def die(self, world: World):
        world.getKilled(self)

    def model(self) -> Model:
        return Model(self.direction, Texture.PACMAN_0, self.position, Vector2Float(0.5, 0.5))
