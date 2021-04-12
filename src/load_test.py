import pygame
import sys

from direction import Direction
from deserialize import Deserialize
from player import Player
from point import Point
from player_controller import PlayerController
from random_controller import RandomController
from renderer import Renderer
from vector2 import Vector2Int
from wall import Wall
from world import World

HEIGHT = 800
WIDTH = 800


def main():
    pygame.init()
    pygame.display.set_caption("Pacman")
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    renderer = Renderer(display)

    playerController = PlayerController()
    deserialize = Deserialize(
            playerController,
            RandomController(),
            RandomController(),
            RandomController(),
            RandomController()
        )
    world = World(Vector2Int(20, 20), deserialize)
    world.loadGrid()

    keys = []
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                keys.append(event.key)
            elif event.type == pygame.KEYUP:
                keys.remove(event.key)

        deltaTime = clock.tick(60) / 1000.0

        playerController.updateKeys(keys)
        world.update(deltaTime)

        renderer.render(world)


if __name__ == '__main__':
    main()