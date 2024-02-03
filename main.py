import pygame as pg
import sys
from pygame.math import Vector2

import utils.player

pg.init()

SCREENSIZE = Vector2(1280, 960)
screen = pg.display.set_mode(SCREENSIZE)
pg.display.set_caption('RoboWars')
buffer_surface = pg.Surface(SCREENSIZE, pg.SRCALPHA)
clock = pg.time.Clock()

font = pg.font.Font('Assets/Fonts/Mono.ttf', 40)

pg.draw.rect(buffer_surface, 'darkgrey', (0, 0, *SCREENSIZE), 40)
for i in range(32):
    pg.draw.line(buffer_surface, 'darkgrey', (0, 40 * i), (1280, 40 * i))
    pg.draw.line(buffer_surface, 'darkgrey', (40 * i, 0), (40 * i, 1280))

buffer_surface = buffer_surface.convert_alpha()


def debug(*args):
    s = " | ".join([str(arg) for arg in args])
    screen.blit(font.render(s, True, 'white', 'black'), (0, 0))


def main():
    player1 = utils.Player(True)
    player2 = utils.Player(False)

    player1.opponent = player2
    player2.opponent = player1

    player1.player_img = player1.player_img.convert_alpha()
    player2.player_img = player2.player_img.convert_alpha()

    zoom = 0.1

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 4:
                    zoom = min((1, zoom+0.01))
                if event.button == 5:
                    zoom = max((0.1, zoom-0.01))

        screen.fill('grey')
        screen.blit(buffer_surface, (0, 0))


        player1.update()
        player2.update()

        player1.draw(screen)
        player2.draw(screen)

        debug(1//(clock.tick(60)*.001))
        pg.display.update()


main()
