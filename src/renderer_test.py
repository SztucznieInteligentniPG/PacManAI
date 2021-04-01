import pygame
import sys

from direction import Direction
from model import Model
from position import Position
from renderer import Renderer
from texture import Texture

clock = pygame.time.Clock()
HEIGHT = 800
WIDTH = 800
BLACK = (0, 0, 0)


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    renderer = Renderer(display)
    pygame.display.set_caption("Pacman")
    animate = 0
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        display.fill(BLACK)
        clock.tick(27)
        a1 = Model(Direction.LEFT, Texture.PACMAN_0, Position(0, 0), Position(0.5, 0.5))
        a2 = Model(Direction.LEFT, Texture.PACMAN_1, Position(4, 0), Position(0.5, 0.5))
        a3 = Model(Direction.LEFT, Texture.PACMAN_2, Position(8, 0), Position(0.5, 0.5))
        renderer.renderModel(a1)
        renderer.renderModel(a2)
        renderer.renderModel(a3)
        pygame.display.flip()
        animate += 1
        if animate >= 27:
            animate = 0
        pygame.display.update()


if __name__ == '__main__':
    main()

