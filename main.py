from random import randint
import pygame as pg

from explosion import Explosion
from fade import Fade
from highlight import Highlight
from revolve import Revolve
from ripple import Ripple
from ripple_generator import RippleGenerator


def loop():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    bg_color = pg.Color(32, 32, 32)

    highlight = Highlight(50, 50, 30, pg.Color("blue"), screen)
    revolve = Revolve(200, 200, 100, 10, pg.Color("yellow"), screen)
    ripple_generator = RippleGenerator(400, 300, 50, 100, 70, 1, pg.Color("red"), screen)

    animations = []
    animations.append(highlight)
    animations.append(ripple_generator)
    animations.append(revolve)

    while True:
        clock.tick(60)
        screen.fill(bg_color)

        for animation in animations:
            if animation.display == False:
                if isinstance(animation, Fade):
                    pg.quit()
                    quit()
                animations.remove(animation)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    animations.append(Fade(0, 255, 2, pg.Color(32, 32, 32), screen))
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                animations.append(Explosion(mouse_x, mouse_y, 30, pg.Color(randint(0, 255), randint(0, 255), randint(0, 255)), screen))

        for animation in animations:
            animation.update()

        for animation in animations:
            animation.render()
        
        pg.display.flip()


if __name__ == '__main__':
    loop()