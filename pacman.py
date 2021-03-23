import pygame
import sys
from pygame.locals import *
Pacman = [pygame.image.load('img/pacman1.png'),
          pygame.image.load('img/pacman2.png'),
          pygame.image.load('img/pacman3.png'),
          ]

clock = pygame.time.Clock()
HEIGHT = 450
WIDTH = 400
BLACK = (0, 0, 0)


def draw_pacman(display, x, y, i):
    display.blit(Pacman[i//9], (x,y))


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
        draw_pacman(display, WIDTH/2-32, HEIGHT/2-32, animate)
        clock.tick(27)
        pygame.display.flip()
        animate += 1
        if animate >= 27:
            animate = 0
        pygame.display.update()


if __name__ == '__main__':
    main()

