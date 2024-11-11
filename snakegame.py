# 05.11.2024

# How to create game
# While TRUE:
    #init
    #draw
    #update

import sys
import pygame
import random

# 1.init game
width = 800
height = 600
pygame.init() # init game environment
screen = pygame.display.set_mode((width,height)) # set up windows
pygame.display.set_caption('My first game') # rename windows title
# todo:add extra init code
# init snake
U_SIZE = 20
snake_img = pygame.image.load('snake.png') # load img
snake_img = pygame.transform.scale(snake_img,(20,20)) # reformat the snake image 20x20
snake_xy = [[40,0],[20,0],[0,0]] # at the beginning there 2 part first part20,0 second part0,0 snake_head=20,0 snake_body=0,0
snake_dir = 'RIGHT' # snake direction -> right
# init food
food_img = pygame.image.load('snake.png')
food_img = pygame.transform.scale(food_img,(20,20))
food_x = random.randrange(0,(width-U_SIZE),U_SIZE)
food_y = random.randrange(0,(height-U_SIZE),U_SIZE)

clock = pygame.time.Clock()
speed = 8
while True:
    # 2.draw game
    # todo:add extra draw code
    screen.fill((0,0,0))
    for snake_x,snake_y in snake_xy:
        screen.blit(snake_img,(snake_x,snake_y))
    screen.blit(food_img,(food_x,food_y))
    # 3.control update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dir = 'UP'
            if event.key == pygame.K_DOWN:
                snake_dir = 'DOWN'
            if event.key == pygame.K_LEFT:
                snake_dir = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake_dir = 'RIGHT'
        # todo: add extra control code
    # 3.1.automatic update
    # todo:add extra update
    # snake moving -> move body ->
    for i in range(len(snake_xy)-1,0,-1):
        snake_xy[i][0] = snake_xy[i-1][0]
        snake_xy[i][1] = snake_xy[i-1][1]
    # snake head definition = snake_xy[0][0] snake_xy[0][1]
    if snake_dir == 'UP':
        snake_xy[0][1] -= 20
    elif snake_dir == 'DOWN':
        snake_xy[0][1] += 20
    elif snake_dir == 'LEFT':
        snake_xy[0][0] -=20
    elif snake_dir =='RIGHT':
        snake_xy[0][0] += 20
    # if the snake catch food
    if snake_xy[0][0] == food_x and snake_xy[0][1] == food_y:
        snake_xy.append([-100,0])
        # create new random food
        food_x = random.randrange(0, (width - U_SIZE), U_SIZE)
        food_y = random.randrange(0, (height - U_SIZE), U_SIZE)
        # snake catches food
        if len(snake_xy) % 3 == 0:
            speed += 2
    clock.tick(speed)
    pygame.display.flip()