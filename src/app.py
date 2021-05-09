import pygame
import sys
import time

from ai_controller import AiController
from deserialize import Deserialize
from game_state import GameState
import network_model
from player_controller import PlayerController
from random_controller import RandomController
from renderer import Renderer
from vector2 import Vector2Int
from world import World

HEIGHT = 800
WIDTH = 800


def main():
    pygame.init()
    pygame.display.set_caption("Pacman")
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    renderer = Renderer(display)

    model = network_model.create()
    # model.load_weights('./training/datetime/best')

    playerController = PlayerController()
    deserialize = Deserialize(
            # playerController,
            AiController(model.get_weights()),
            RandomController(),
            RandomController(),
            RandomController(),
            RandomController(),
        )
    world = World(Vector2Int(19, 19), deserialize, True)
    world.loadGrid()

    safeDeltaTime = world.maximumSafeUpdateTime()

    keys = []
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif world.gameState == GameState.WON:
                print('you won')
                time.sleep(1)
                pygame.quit()
                sys.exit(0)
            elif world.gameState == GameState.LOST:
                print('you lost')
                time.sleep(1)
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                keys.append(event.key)
            elif event.type == pygame.KEYUP:
                keys.remove(event.key)

        deltaTime = clock.tick(60) / 1000.0
        deltaTime = safeDeltaTime if deltaTime > safeDeltaTime else deltaTime

        playerController.updateKeys(keys)
        world.update(deltaTime)

        renderer.render(world)


def trainPlayer(weights) -> int:
    deserialize = Deserialize(
            AiController(weights),
            RandomController(),
            RandomController(),
            RandomController(),
            RandomController(),
        )
    world = World(Vector2Int(19, 19), deserialize)
    world.loadGrid()

    deltaTime = world.maximumSafeUpdateTime()

    while True:
        if world.gameState == GameState.WON or world.gameState == GameState.LOST:
            break

        world.update(deltaTime)

    return world.score


if __name__ == '__main__':
    main()
