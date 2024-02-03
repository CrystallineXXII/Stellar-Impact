import pygame as pg
from pygame.math import Vector2


class Player:
    def __init__(self, n):

        self.player_img = pg.transform.rotozoom(pg.image.load(
            "Assets/Images/blue_sniper.png" if n else "Assets/Images/red_sniper.png"), 0, 0.5)

        self.pos = Vector2(640, 680 if n else 280)
        self.vel = Vector2()
        self.facing = 0 if n else 180
        self.n = n

        self.fire = False
        self.shockers = (Vector2(-60, -80), Vector2(60, -80))

        self.opponent = None

    def update(self):
        self.vel = Vector2()
        self.fire = False

        keys = pg.key.get_pressed()
        if keys[pg.K_w if self.n else pg.K_i]:
            self.vel += Vector2(0, -1)
            self.fire = True
        if keys[pg.K_s if self.n else pg.K_k]:
            self.vel += Vector2(0, 1)
        if keys[pg.K_a if self.n else pg.K_j]:
            self.facing += 2
        if keys[pg.K_d if self.n else pg.K_l]:
            self.facing -= 2

        self.vel = self.vel.normalize() if self.vel.length() > 0 else self.vel
        self.facing %= 360

        self.pos += self.vel.rotate(-self.facing) * 3
        self.pos.x = min((max((80, self.pos.x)), 1200))
        self.pos.y = min((max((80, self.pos.y)), 880))

    def draw(self, screen):
        image = pg.transform.rotozoom(self.player_img, self.facing, 1)
        img_rect = image.get_rect(center=self.pos + Vector2(0, -50 * 0.5).rotate(-self.facing))

        if self.fire:
            pg.draw.line(screen, 'blue' if self.n else 'red', self.shockers[0].rotate(-self.facing) + self.pos,
                         self.shockers[1].rotate(-self.facing) + self.pos, 5)

        screen.blit(image, img_rect)
