from direction import Direction
from mock_controller import MockController
from player import Player
from wall import Wall
from world import World
from world_position import WorldPosition


world = World(WorldPosition(4, 4))

player = Player(MockController(Direction.LEFT), Direction.LEFT)
world.putEntity(Wall(), WorldPosition(1, 1))

world.putEntity(player, WorldPosition(3, 1))

# test ściany
print(player.position, player.worldPosition)
player.update(world, 0.5)
print(player.position, player.worldPosition)
player.update(world, 0.5)
print(player.position, player.worldPosition)
player.update(world, 0.5)
print(player.position, player.worldPosition)

print()

# test końca poziomu
player.controller = MockController(Direction.UP)
player.update(world, 0.5)
print(player.position, player.worldPosition)
player.update(world, 0.5)
print(player.position, player.worldPosition)
player.update(world, 0.5)
print(player.position, player.worldPosition)

print()

player.controller = MockController(Direction.LEFT)
player.update(world, 1)
print(player.position, player.worldPosition)
player.update(world, 1)
print(player.position, player.worldPosition)
player.update(world, 1)
print(player.position, player.worldPosition)
