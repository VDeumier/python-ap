import pygame as pg

pg.init()

framerate = 5

#Background parameters
bg_color = (87, 130, 52)
brighter_col = (87, 200, 52)
snake_col = (40, 70, 130)
sc_height = 300                          
sc_width = 400

#Checkers parameters
nbr_hor_squares = 20
nbr_ver_squares = 15
sq_width = sc_width/nbr_hor_squares
sq_height = sc_height/nbr_ver_squares
X = [i*sq_width for i in range(nbr_hor_squares)]
Y = [i*sq_height for i in range(nbr_ver_squares)]

#Snake intialization
'''
Le serpent est stocké dans une liste contenant les coordonées et directions de chaque carré 
le composant afin de pouvoir aumgenter la taille du serpent par la queue lorsqu'il mange un fruit
'''
snake = [[[7, 9], 'right'], [[6, 9], 'right'], [[5, 9], 'right']]                        # snake = [head, ..., tail]

screen = pg.display.set_mode((sc_width, sc_height))
clock = pg.time.Clock()
flag = True

def snake_step(snake):

    for i in snake:
        if i[1] == 'right':
            i[0][0] += 1
        elif i[1] == 'left':
            i[0][0] -= 1
        elif i[1] == 'up':
            i[0][1] -= 1
        else:
            i[0][1] += 1

def snake_dir_propagation(snake):

    for i in range(len(snake)-1, 0, -1):
        snake[i][1] = snake[i-1][1]


while flag:

    screen.fill(bg_color)                                           # draw background

    for i in range(nbr_hor_squares):                                # draw checkers
        for j in range(nbr_ver_squares):    
            if (i+j)%2 == 1:       
                rect = pg.Rect(X[i], Y[j], sq_width, sq_height)
                pg.draw.rect(screen, brighter_col, rect)

    for p in snake:                                                 # draw snake 
        rect = pg.Rect(X[p[0][0]], Y[p[0][1]], sq_width, sq_height)
        pg.draw.rect(screen, snake_col, rect)

    for event in pg.event.get():

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:                                 #quit game window
                flag = False
            if event.key == pg.K_UP:                                #direction input
                snake[0][1] = 'up'
            if event.key == pg.K_DOWN:
                snake[0][1] = 'down'
            if event.key == pg.K_RIGHT:
                snake[0][1] = 'right'
            if event.key == pg.K_LEFT:
                snake[0][1] = 'left'

    snake_step(snake)
    snake_dir_propagation(snake)

    pg.display.update()
    clock.tick(framerate)

pg.quit()