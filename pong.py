import pygame
import random
from pygame.locals import *
pygame.init()
random.seed()

screen = pygame.display.set_mode((400, 400))
sprite_ball = pygame.image.load("sprites/ball.png")
sprite_paddle1 = pygame.image.load("sprites/paddle.png")
sprite_paddle2 = pygame.image.load("sprites/paddle.png")

rect_paddle1 = sprite_paddle1.get_rect()
rect_paddle2 = sprite_paddle2.get_rect()
rect_ball = sprite_ball.get_rect()

rect_ball.left = 187.5
rect_ball.top = 187.5
rect_paddle1.left = 150
rect_paddle1.top = 0

rect_paddle2.left = 150
rect_paddle2.top = 375

hspeed = 0
vspeed = 0
while hspeed == 0:
    hspeed = random.randint(-1, 1)
    hspeed = hspeed
while vspeed == 0:
    vspeed = random.randint(-1, 1)
    vpseed = vspeed
slower = 1

run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(sprite_ball, rect_ball)
    screen.blit(sprite_paddle1, rect_paddle1)
    screen.blit(sprite_paddle2, rect_paddle2)
    pygame.display.flip()
    #game logic
    slower -= 1
    if slower == 0:
        slower = 1
        if hspeed < 0:
            if (rect_ball.left + hspeed > 0):
                rect_ball.left += hspeed
            else:
                hspeed = -hspeed
        else:
            if (rect_ball.left + hspeed < 375):
                rect_ball.left += hspeed
            else:
                hspeed = -hspeed
        #vertical movement for ball
        if vspeed < 0:
            if (rect_ball.top + vspeed > 0):
                rect_ball.top += vspeed
            else:
                rect_ball.left = 200 - 12.5
                rect_ball.top = 200 - 12.5
        else:
            if (rect_ball.top + vspeed < 375):
                rect_ball.top += vspeed
            else:
                rect_ball.left = 200 - 12.5
                rect_ball.top = 200 - 12.5
    #ball collision with paddle1
    coll = False
    if ((rect_ball.left >= rect_paddle1.left) and (rect_ball.left <= rect_paddle1.left + rect_paddle1.width) and (rect_ball.top >= rect_paddle1.top) and (rect_ball.top <= rect_paddle1.top + rect_paddle1.height)):
        coll = True
    elif ((rect_paddle1.left >= rect_ball.left) and (rect_paddle1.left <= rect_ball.left + rect_ball.width) and (rect_paddle1.top >= rect_ball.top) and (rect_paddle1.top <= rect_ball.top + rect_ball.height)):
        coll = True
    #ball collision with paddle2
    if ((rect_ball.left >= rect_paddle2.left) and (rect_ball.left <= rect_paddle2.left + rect_paddle2.width) and (rect_ball.top + rect_ball.height >= rect_paddle2.top) and (rect_ball.top + rect_ball.height <= rect_paddle2.top + rect_paddle2.height)):
        coll = True
    elif ((rect_paddle2.left >= rect_ball.left) and (rect_paddle2.left <= rect_ball.left + rect_ball.width) and (rect_paddle2.top >= rect_ball.top) and (rect_paddle2.top <= rect_ball.top + rect_ball.height)):
        coll = True

    if coll:
        if ((rect_ball.top < 200) and (vspeed < 0)):
            vspeed = -vspeed
        elif ((rect_ball.top > 200) and (vspeed > 0)):
            vspeed = -vspeed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        #left is pressed
        if (rect_paddle1.left > 0):
            rect_paddle1.left -= 1
    if keys[pygame.K_RIGHT]:
        #a is pressed
        if (rect_paddle1.right < 400):
            rect_paddle1.left += 1
    if keys[pygame.K_s]:
        #a is pressed
        if (rect_paddle2.right < 400):
            rect_paddle2.left += 1
    if keys[pygame.K_a]:
        #a is pressed
        if (rect_paddle2.left > 0):
            rect_paddle2.left -= 1
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
pygame.quit()
