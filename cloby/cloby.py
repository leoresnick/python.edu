#!/usr/bin/python
import pygame
import time
import datetime
import sys

pygame.init()
cloby_size = 32
cloby_pad = 4
cloby_disp_res = cloby_width, cloby_height = cloby_size*8, cloby_size
cloby_bg_color = 0, 0, 255
cloby_sym_color_on = 255, 255, 255
cloby_sym_color_off = 0, 0, 0
cloby_sym_size = cloby_size-cloby_pad*2
cloby_disp = pygame.display.set_mode( cloby_disp_res,
                                    pygame.HWSURFACE |
                                    #pygame.FULLSCREEN |
                                    pygame.DOUBLEBUF |
                                    pygame.NOFRAME
                                    )
ticking=True
divs = ( 43200, 21600, 10800, 5400, 2700, 1350, 675, 337.5 )
print( divs[0], divs[7] )
while ticking:
    for event in pygame.event.get():
        #print( event.type )
        if event.type in ( pygame.MOUSEBUTTONDOWN, pygame.QUIT ): ticking = False
    cloby_today = datetime.datetime.today()
    cloby_time = cloby_today.hour * 3600 + cloby_today.minute * 60 + cloby_today.second
    cloby_disp.fill( cloby_bg_color )
    for b in range( 0, 8) :
        tmp_time = cloby_time // divs[b]
        print( b," - ", divs[b]," = ", tmp_time )
        if tmp_time == 1 : dig_color = cloby_sym_color_on
        else : dig_color = cloby_sym_color_off
        cloby_disp.fill( dig_color, ( (cloby_size * b) + cloby_pad, cloby_pad, cloby_sym_size, cloby_sym_size), 0 )
        cloby_time = cloby_time - tmp_time * divs[b]
	#print( cloby_time )
    #pygame.surface.rect(cloby_disp, cloby_sym_color, cloby_sym_size, 0)
    pygame.display.flip()
    time.sleep(1)
