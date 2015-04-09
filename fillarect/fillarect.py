#!/usr/bin/python
import pygame
import random
import sys

pygame.init()
pygame.display.set_icon( pygame.image.load( 'fillarect.png' ) )
pygame.display.set_caption('Fill-A-Rect. Controls are: (M)aximize/(R)estore window, (F)ullscreen, (Q)uit')
disinf = pygame.display.Info()
dismaxx = disinf.current_w
dismaxy = disinf.current_h
fsmaxxy = pygame.display.list_modes(0, pygame.FULLSCREEN)[0]
print fsmaxxy
screen = pygame.display.set_mode((dismaxx, dismaxy),pygame.RESIZABLE)
run = True
while run:
    for event in pygame.event.get():
        print event
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_m :
                lastmaxx = dismaxx
                lastmaxy = dismaxy
                dismaxx = disinf.current_w
                dismaxy = disinf.current_h
                pygame.display.set_mode((dismaxx,dismaxy),pygame.RESIZABLE)
            if event.key == pygame.K_r :
                dismaxx = lastmaxx
                dismaxy = lastmaxy
                pygame.display.set_mode((dismaxx,dismaxy),pygame.RESIZABLE)
            if event.key == pygame.K_f :
                if screen.get_flags() & pygame.FULLSCREEN:
                    dismaxx = winmaxx
                    dismaxy = winmaxy
                    pygame.display.set_mode((winmaxx, winmaxy),pygame.RESIZABLE)
                else:
                    winmaxx = dismaxx
                    winmaxy = dismaxy
                    dismaxx = fsmaxxy[0]
                    dismaxy = fsmaxxy[1]
                    pygame.display.set_mode(fsmaxxy, pygame.FULLSCREEN)
                print 'f pressd'
            if event.key == pygame.K_q :
				run = False
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.VIDEORESIZE :
            dismaxx = event.size[0]
            dismaxy = event.size[1]
            pygame.display.set_mode((dismaxx, dismaxy),pygame.RESIZABLE)
    kv_color = random.randint( 0, 255 ), random.randint( 0, 255 ), random.randint( 0, 255 )
    kv_x = random.randint( 0, dismaxx )
    kv_y = random.randint( 0, dismaxy )
    kv_dx = random.randint( 0, dismaxx - kv_x )
    kv_dy = random.randint( 0, dismaxy - kv_y )
    screen.fill( kv_color, (kv_x, kv_y, kv_dx, kv_dy) )
    pygame.display.flip()
