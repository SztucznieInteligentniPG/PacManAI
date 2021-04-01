import pygame
import sys
from model import Model
from renderer import Renderer

from direction import Direction
from position import Position
from texture import Texture

clock = pygame.time.Clock()
HEIGHT = 800
WIDTH = 800
BLACK = (0, 0, 0)


r = Renderer()


def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")
    animate = 0
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        display.fill(BLACK)
        clock.tick(27)
        a = Model(Direction.UP, Texture.PACMAN, Position(0,0), Position(0.5, 0.5))
        r.render(a, display, animate//9)
        pygame.display.flip()
        animate += 1
        if animate >= 27:
            animate = 0
        pygame.display.update()


if __name__ == '__main__':
    main()

