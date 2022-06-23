from turtle import color
import numpy as np
import pygame
import fractal_engine as fe
from pygame import gfxdraw


import sys 
from colour import Color

black = Color(rgb=(0, 0, 0))
red = Color(rgb=(1, 0, 0)) 
green = Color(rgb=(0, 1, 0))
blue = Color(rgb=(0, 0, 1))
white = Color(rgb=(1, 1, 1))

pallete = []

iter = 150 #how much we should iterate

print(sys.argv)

if len(sys.argv) == 1:


    for i in range(iter):
        color_step = 255/iter
        pallete.append((color_step*i,color_step*i,color_step*i))


elif len(sys.argv) > 1:

    print('MORE THAN 2')

    if sys.argv[1] == 'green':
        grad = []
        grad = list(black.range_to(green, iter))

    elif sys.argv[1] == 'fire':
        grad = []
        grad = list(black.range_to(red, iter))

    elif sys.argv[1] == 'alternate':
        grad =[]
        for i in range(iter):
            if (i % 2 == 0):
                grad.append(black)
            elif (i % 2 == 1):
                grad.append(white)

    for color in grad:
        print(color.rgb)
        pallete.append((color.red*255, color.green *255, color.blue * 255))

#---------------------------------------------------------------------------


pygame.init()
clock = pygame.time.Clock() #pygame clock for fps

width = 400 # screen parameters
height = 400

screen = pygame.display.set_mode([width, height]) #init screen and fill it
screen.fill((0, 0, 0))

zoom = 4 #arbitrary number
dr = zoom/width #set difference in real part
di = -zoom/height #set difference in imag part

anchor_pos = -2+2j #anchor position top left


def px_to_coord(pos): # translate a pixel coordinate from the screen to a cartesian coordinate using steps an an anchor point
    x , y = pos #pos tuple broken to vars x and y

    real_part = anchor_pos.real + dr * x #anchor pos + steps(dr || di) * pixels pos
    imag_part = anchor_pos.imag + di * y
    
    return(real_part+imag_part*1j)


def init_coords(res = 1): # res stands for resolution you can turn it to 2 in order to cut the resolution in half. init coords with desired resolution
    number_plain = np.ones((width,height),dtype=tuple) #numpy array maps every pixel to coordinate

    res = int(res)

    w = int(width/res)
    h = int(height/res)


    for i in range(w):
        for q in range(h):

            for a in range(res):
                number_plain[res*i-a][res*q]   = (i * res , q * res)
                for b in range(res):
                    number_plain[res*i-a][res*q - b]   = (i * res , q * res)


    vfunc = np.vectorize(px_to_coord) 
    array = vfunc(number_plain)# maps each pixel coordinate to an imaginary coordinate using numpys vectorize function
    
    return array

if __name__ == "__main__":

    running = 1 

    mapped_numbers = init_coords()

    drag = False

    

    while running:

        #start_time = time.time()
        #print("STARTING TIME")

        m_pos = pygame.mouse.get_rel()
        rel_x ,rel_y = m_pos
        
        clock.tick(60)     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drag = True
                    
                            
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drag = False
                    mapped_numbers = init_coords(1)

                    
            elif event.type == pygame.MOUSEMOTION:
                if drag:
                    
                    anchor_pos -= dr * rel_x 
                    anchor_pos -= di * rel_y * 1j

                    mapped_numbers = init_coords(2)

            elif event.type == pygame.MOUSEWHEEL:
                

                if event.y > 0:
                    zoom *= 0.9

                elif event.y <0:
                    zoom *=1.1

                else:
                    mapped_numbers = init_coords(1)

                dr = zoom/width #set difference in real part
                di = -zoom/height #set difference in imag part
                    
                mapped_numbers = init_coords(2)

        for i in range(width):
            for q in range(height):
                z_n = mapped_numbers[i][q]
                intese = fe.repeat_iteration(z_n,iter)
                gfxdraw.pixel(screen,i,q,pallete[intese])

            
        

        #total_time = time.time() - start_time
        #print(str(total_time )+": SECONDS")
        pygame.display.flip()       

    pygame.quit()

    


