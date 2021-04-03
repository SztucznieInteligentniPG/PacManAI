import pygame
import sys

from direction import Direction
from model import Model
from renderer import Renderer
from texture import Texture
from vector2 import Vector2Int

clock = pygame.time.Clock()
HEIGHT = 800
WIDTH = 800
BACKGROUND = (0, 0, 0)


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    renderer = Renderer(display)
    pygame.display.set_caption("Pacman")

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        display.fill(BACKGROUND)
        clock.tick(27)

        a1 = Model(Direction.LEFT, Texture.PACMAN_0, Vector2Int(0, 0), Vector2Int(0.5, 0.5))
        a2 = Model(Direction.LEFT, Texture.PACMAN_1, Vector2Int(4, 0), Vector2Int(0.5, 0.5))
        a3 = Model(Direction.LEFT, Texture.PACMAN_2, Vector2Int(8, 0), Vector2Int(0.5, 0.5))

        renderer.renderModel(a1)
        renderer.renderModel(a2)
        renderer.renderModel(a3)

        pygame.display.update()


if __name__ == '__main__':
    main()
