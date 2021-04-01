import pygame
import sys
from model import Model
from renderer import Renderer

from src.direction import Direction
from src.position import Position
from src.texture import Texture

clock = pygame.time.Clock()
HEIGHT = 450
WIDTH = 400
BLACK = (0, 0, 0)


a = Model(Direction.UP, Texture.PACMAN, Position(30, 30), Position(0, 0))
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
        r.render(a, display, animate//9)
        pygame.display.flip()
        animate += 1
        if animate >= 27:
            animate = 0
        pygame.display.update()


if __name__ == '__main__':
    main()

