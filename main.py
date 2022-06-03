import numpy as np
from numpy import imag, number, real
import pygame
import fractal_engine as fe
import time
from pygame import gfxdraw


pygame.init()
clock = pygame.time.Clock() #pygame clock for fps

width = 600 # screen parameters
height = 600

screen = pygame.display.set_mode([width, height]) #init screen and fill it
screen.fill((0, 0, 0))

zoom = 4 #arbitrary number
dr = zoom/width #set difference in real part
di = -zoom/height #set difference in imag part

def px_to_coord(pos): # translate a pixel coordinate from the screen to a cartesian coordinate using steps an an anchor point
    x , y = pos #pos tuple broken to vars x and y

    anchor_pos = -2+2j #anchor position top left

    real_part = anchor_pos.real + dr * x #anchor pos + steps(dr || di) * pixels pos
    imag_part = anchor_pos.imag + di * y


    return(real_part+imag_part*1j)


running = 1 

number_plain = np.ones((width,height),dtype=tuple) #numpy array maps every pixel to coordinate

for i in range(width):
    for q in range(height):
        number_plain[i][q] = (i , q) #run through array and set val to a pixel coordinate from the screen


vfunc = np.vectorize(px_to_coord) 
mapped_numbers = vfunc(number_plain)# maps each pixel coordinate to an imaginary coordinate using numpys vectorize function

while running:

    
    clock.tick(60)     
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False

    for i in range(width):
        for q in range(height):
            z_n = mapped_numbers[i][q]
            color = fe.repeat_iteration(z_n,25)
            gfxdraw.pixel(screen,i,q,(2.55*color,2.55*color,2.55*color))

    
    pygame.display.flip()       

pygame.quit()


