from turtle import color
import numpy as np
import pygame
import fractal_engine as fe
from pygame import gfxdraw

pallete = []

for i in range(500):
    pallete.append(((i/500)*255,(i/500)*255,(i/500)*255))


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

iter = 500 #how many times to iterate

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
                intese = fe.repeat_iteration(z_n,500)
                gfxdraw.pixel(screen,i,q,pallete[intese])

            
        

        #total_time = time.time() - start_time
        #print(str(total_time )+": SECONDS")
        pygame.display.flip()       

    pygame.quit()

    


