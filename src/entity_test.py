from direction import Direction
from mock_controller import MockController
from player import Player
from wall import Wall
from world import World
from world_position import WorldPosition


world = World(WorldPosition(4, 4))

player = Player(MockController(Direction.LEFT), Direction.LEFT)
wall = Wall()
world.putEntity(wall, WorldPosition(1, 1))
world.putActor(player, WorldPosition(3, 1))

print(world.actors)
print(world.grid)

print('test ściany')

print(player.position, player.worldPosition)
world.update(0.5)
print(player.position, player.worldPosition)
world.update(0.5)
print(player.position, player.worldPosition)
world.update(0.5)
print(player.position, player.worldPosition)

print('test końca poziomu')
print('krawędź górna')

player.controller = MockController(Direction.UP)
world.update(0.7)
print(player.position, player.worldPosition)
world.update(0.7)
print(player.position, player.worldPosition)
world.update(0.7)
print(player.position, player.worldPosition)

print('krawędź lewa')

player.controller = MockController(Direction.LEFT)
world.update(1)
print(player.position, player.worldPosition)
world.update(1)
print(player.position, player.worldPosition)
world.update(1)
print(player.position, player.worldPosition)

wall.destroy(world)
player.destroy(world)

print(world.actors)
print(world.grid)
