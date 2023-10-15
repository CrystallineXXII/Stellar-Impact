import pygame as pg
import sys
from pygame.math import Vector2

pg.init()

SCREENSIZE = Vector2(1280, 960)
screen = pg.display.set_mode(SCREENSIZE)
buffer_surface = pg.Surface(SCREENSIZE)


def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        buffer_surface.fill((0, 0, 0))
        pg.draw.circle(buffer_surface, (255, 0, 0), SCREENSIZE / 2, 50)
        screen.blit(buffer_surface, (0, 0))
        pg.display.update()

main()