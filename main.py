import pygame as pg

from highlight import Highlight


def loop():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    bg_color = pg.Color(32, 32, 32)

    highlight = Highlight(50, 50, 30, pg.Color("blue"), screen)

    while True:
        clock.tick(60)
        screen.fill(bg_color)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        highlight.update()

        highlight.render()
            
        
        pg.display.flip()


if __name__ == '__main__':
    loop()