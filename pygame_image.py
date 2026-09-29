import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton_img = pg.image.load("fig/3.png")
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    bg_img2 = pg.transform.flip(bg_img, True, False)
    koukaton_rct = koukaton_img.get_rect()
    koukaton_rct.center = (300, 200)
    
    screen.blit(koukaton_img, koukaton_rct)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        key_lst = pg.key.get_pressed()
        sx = -1
        sy =0

        if key_lst[pg.K_UP]:
                sx += 0
                sy += -1
        elif key_lst[pg.K_DOWN]:
                sx += 0
                sy += 1
        elif key_lst[pg.K_LEFT]:
                sx = -1
                sy = 0
        elif key_lst[pg.K_RIGHT]:
                sx = +1
                sy = 0

        koukaton_rct.move_ip((sx, sy))

        screen.blit(bg_img, [0 - x, 0])
        screen.blit(bg_img2, [1600 - x, 0])
        screen.blit(bg_img, [3200 - x, 0])
        screen.blit(koukaton_img, [koukaton_rct.x, koukaton_rct.y])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()