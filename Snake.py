import pygame as pg
import random as rd

pg.init()
pg.font.init()

framerate = 6

#Background parameters
bg_color = (87, 130, 52)
brighter_col = (87, 200, 52)
sc_height = 600
sc_width = 800

#Checkers parameters
nbr_hor_squares = 20
nbr_ver_squares = 15
sq_width = sc_width/nbr_hor_squares
sq_height = sc_height/nbr_ver_squares
X = [i*sq_width for i in range(nbr_hor_squares)]
Y = [i*sq_height for i in range(nbr_ver_squares)]

#Fruit parameters
fruit_col = (220, 40, 50)

#Snake parameters
snake = [(7, 9), (6, 9), (5, 9)]                        # snake = [head, ..., tail]
snake_dir = 'right'
snake_col = (40, 70, 130)

#Score parameters
score = 0
score_incr = 1

screen = pg.display.set_mode((sc_width, sc_height))
clock = pg.time.Clock()
flag = True

def snake_step(snake):
    snake.pop()
    if snake_dir == 'right':
        snake.insert(0, (snake[0][0]+1, snake[0][1]))
    elif snake_dir == 'left':
        snake.insert(0, (snake[0][0]-1, snake[0][1]))
    elif snake_dir == 'up':
        snake.insert(0, (snake[0][0], snake[0][1]-1))
    else:
        snake.insert(0,(snake[0][0], snake[0][1]+1))


def random_fruit():
    return (X[rd.randrange(nbr_hor_squares)],Y[rd.randrange(nbr_ver_squares)])

fruit = random_fruit()

while flag:

    head = snake[0]
    tail = snake[-1]

    if (X[head[0]], Y[head[1]]) == fruit:                     # interaction with fruit        
        snake.append(tail)
        score += score_incr       
        fruit = random_fruit()

    screen.fill(bg_color)                                           # draw background

    for i in range(nbr_hor_squares):                                # draw checkers
        for j in range(nbr_ver_squares):    
            if (i+j)%2 == 1:       
                rect = pg.Rect(X[i], Y[j], sq_width, sq_height)
                pg.draw.rect(screen, brighter_col, rect)

    for p in snake:                                                 # draw snake 
        rect = pg.Rect(X[p[0]], Y[p[1]], sq_width, sq_height)
        pg.draw.rect(screen, snake_col, rect)

    rect = pg.Rect(fruit[0], fruit[1], sq_width, sq_height)         # draw fruit
    pg.draw.rect(screen, fruit_col, rect)                       

    font = pg.font.Font(None, 56)                                   # display score
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    for event in pg.event.get():

        if event.type == pg.QUIT:                                   #quit game window
            flag = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:                                 
                flag = False
            if event.key == pg.K_UP:                                #direction input
                snake_dir = 'up'
            if event.key == pg.K_DOWN:
                snake_dir = 'down'
            if event.key == pg.K_RIGHT:
                snake_dir = 'right'
            if event.key == pg.K_LEFT:
                snake_dir = 'left'

    head = snake[0]
    tail = snake[-1]

    if head[0] == 0 and snake_dir == 'left':                      #Exit if collision with the border
        flag = False
    if head[0] == nbr_hor_squares-1 and snake_dir == 'right':
        flag = False
    if head[1] == 0 and snake_dir == 'up':
        flag = False
    if head[1] == nbr_ver_squares-1 and snake_dir == 'down':
        flag = False

    for i in range(1, len(snake)):                                 #Exit if collision with self
        if head == snake[i]:
            flag = False

    snake_step(snake)                                              # Update snake position 

    pg.display.update()
    clock.tick(framerate)

pg.quit()