import pygame as pg
import random as rd
import copy

pg.init()

framerate = 7

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

def random_fruit():
    return [X[rd.randrange(nbr_hor_squares)],Y[rd.randrange(nbr_ver_squares)]]

fruit = random_fruit()

while flag:

    head = snake[0]
    tail = snake[-1]

    if [X[head[0][0]], Y[head[0][1]]] == fruit:                     # interaction with fruit
        
        new_tail = copy.deepcopy(tail)
        if tail[1] == 'right':
            new_tail[0][0] -= 1
        elif tail[1] == 'left':
            new_tail[0][0] += 1
        elif tail[1] == 'up':
            new_tail[0][1] += 1
        else:
            new_tail[0][1] -= 1 
        snake.append(new_tail)
        
        fruit = random_fruit()

    screen.fill(bg_color)                                           # draw background

    for i in range(nbr_hor_squares):                                # draw checkers
        for j in range(nbr_ver_squares):    
            if (i+j)%2 == 1:       
                rect = pg.Rect(X[i], Y[j], sq_width, sq_height)
                pg.draw.rect(screen, brighter_col, rect)

    for p in snake:                                                 # draw snake 
        rect = pg.Rect(X[p[0][0]], Y[p[0][1]], sq_width, sq_height)
        pg.draw.rect(screen, snake_col, rect)

    rect = pg.Rect(fruit[0], fruit[1], sq_width, sq_height)
    pg.draw.rect(screen, (220, 40, 50), rect)                       # draw fruit

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

    head = snake[0]
    tail = snake[-1]

    if head[0][0] == 0 and head[1] == 'left':                      #Exit if collision with the border
        flag = False
    if head[0][0] == nbr_hor_squares-1 and head[1] == 'right':
        flag = False
    if head[0][1] == 0 and head[1] == 'up':
        flag = False
    if head[0][1] == nbr_ver_squares-1 and head[1] == 'down':
        flag = False

    for i in range(1, len(snake)):                                 #Exit if collision with self
        if head[0] == snake[i][0]:
            flag = False

    snake_step(snake)
    snake_dir_propagation(snake)

    pg.display.update()
    clock.tick(framerate)

pg.quit()