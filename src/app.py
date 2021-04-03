import pygame
import sys

from direction import Direction
from player import Player
from random_controller import RandomController
from renderer import Renderer
from wall import Wall
from world import World
from world_position import WorldPosition

HEIGHT = 800
WIDTH = 800


def main():
    pygame.init()
    pygame.display.set_caption("Pacman")
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    renderer = Renderer(display)
    world = World(WorldPosition(20, 20))

    player = Player(RandomController(), Direction.UP)

    world.putEntity(Wall(), WorldPosition(5, 7))
    world.putEntity(Wall(), WorldPosition(5, 8))
    world.putEntity(Wall(), WorldPosition(5, 9))
    world.putEntity(Wall(), WorldPosition(6, 9))
    world.putEntity(Wall(), WorldPosition(7, 9))
    world.putEntity(Wall(), WorldPosition(5, 10))
    world.putEntity(Wall(), WorldPosition(5, 11))
    world.putActor(player, WorldPosition(10, 10))

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        deltaTime: float = clock.tick(60) / 1000.0

        world.update(deltaTime)

        renderer.render(world)


if __name__ == '__main__':
    main()
