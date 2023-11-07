import pygame as pg

pg.init()

framerate = 24
bg_color = (87, 130, 52)
brighter_col = (87, 200, 52)
sc_height = 300                          
sc_width = 400
nbr_hor_squares = 20
nbr_ver_squares = 15
sq_width = sc_width/nbr_hor_squares
sq_height = sc_height/nbr_ver_squares


screen = pg.display.set_mode((sc_width, sc_height))
clock = pg.time.Clock()
flag = True

while flag:

    screen.fill(bg_color)                                       #background color
    left = 0
    top = 0

    for i in range(nbr_hor_squares//2):                            #checkers setup
        for j in range(nbr_ver_squares//2):           
            rect = pg.Rect(left, top, sq_width, sq_height)
            pg.draw.rect(screen, brighter_col, rect)
            top += 2*sq_height
        left += 2*sq_width

    for event in pg.event.get():

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                flag = False

    pg.display.update()
    clock.tick(framerate)

pg.quit()