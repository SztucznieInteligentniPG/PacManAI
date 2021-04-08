import pygame
import sys

from direction import Direction
from player import Player
from player_controller import PlayerController
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
    world = World(Vector2Int(20, 20))

    playerController = PlayerController()
    player = Player(playerController, Direction.UP)

    world.putEntity(Wall(), Vector2Int(5, 7))
    world.putEntity(Wall(), Vector2Int(5, 8))
    world.putEntity(Wall(), Vector2Int(5, 9))
    world.putEntity(Wall(), Vector2Int(6, 9))
    world.putEntity(Wall(), Vector2Int(7, 9))
    world.putEntity(Wall(), Vector2Int(5, 10))
    world.putEntity(Wall(), Vector2Int(4, 10))
    world.putEntity(Wall(), Vector2Int(5, 11))
    world.putActor(player, Vector2Int(10, 10))

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
