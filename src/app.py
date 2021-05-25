import math
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

HEIGHT = 700
WIDTH = 648


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Pacman")
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    renderer = Renderer(display)

    model = network_model.create()
    model.load_weights('./training/best')
    seed = 1

    playerController = PlayerController()
    deserialize = Deserialize(
            # playerController,
            AiController(model.get_weights()),
            RandomController(1, seed),
            RandomController(1, seed + 1),
            RandomController(1, seed + 2),
            RandomController(1, seed + 3),
        )
    world = World(Vector2Int(19, 19), deserialize, True)
    world.loadGrid()

    realTimeMultiplier = 1
    baseTickRate = world.tickRate()
    tickRate = int(math.ceil(60 / realTimeMultiplier / baseTickRate)) * baseTickRate

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

        clock.tick(tickRate * realTimeMultiplier)

        playerController.updateKeys(keys)
        world.update(tickRate)

        renderer.render(world)


def trainPlayer(weights: list, seed: int) -> int:

    deserialize = Deserialize(
            AiController(weights),
            RandomController(2, seed),
            RandomController(2, seed + 1),
            RandomController(2, seed + 2),
            RandomController(2, seed + 3),
        )
    world = World(Vector2Int(19, 19), deserialize)
    world.loadGrid()

    tickRate = world.tickRate()

    while True:
        if world.gameState == GameState.WON or world.gameState == GameState.LOST:
            break

        world.update(tickRate)

    return world.score


if __name__ == '__main__':
    main()
