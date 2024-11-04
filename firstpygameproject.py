# 04.11.2024

import sys
import pygame

# models of pygame
# pygame.display # show model
# pygame.draw #
# pygame.image # image model
# pygame.event # event model tastatur maus
# pygame.mixer # media model

# 1.init game environment
pygame.init() # init game environment
# 500 x 700 - width = 500 & length = 700
screen = pygame.display.set_mode((500,700)) # create window set up format 500x700
rect = pygame.Rect(100,200,60,60) # init a rectangle surface
# todo: insert init code
# add new function
img = pygame.image.load('sunqian.jpg')
new_img = pygame.transform.scale(img,(50,70)) # redefine the dimension of the img
new_rect = pygame.Rect(400,100,50,70) # init a rect surface
new_rect.center = 425,135 # coordinate of the new_rect
# pygame.mixer.music.load('add music path') # add background music
# music_v = 0.5 # init voice
# pygame.mixer.music.set_volume(music_v) # set up voice
# pygame.mixer.music.play(-1) # -1 replay music

while True:
    # 2.design game interface
    pygame.draw.rect(screen,'gold',rect)
    # todo: insert code to draw surface
    # new_rect = new_img.get_rect()
    screen.blit(new_img,new_rect)

    # 3.1 data update - manuell update
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # todo:insert control code - aktions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if music_v >= 0.1:
                    music_v -= 0.1
            if event.key == pygame.K_UP:
                if music_v < 1:
                    music_v += 0.1
    # 3.2 data update - automatic
    pygame.display.update()
    # todo:insert automatic update code

