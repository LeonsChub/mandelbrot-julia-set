import pygame
import fractal_engine
from gradient import palette
import time
from concurrent.futures import ThreadPoolExecutor
import threading
from numba import jit,njit

FIRE = palette([[[0,0,0],230*1],[[255,0,0],230*2],[[255,255,0],230*3],[[255,255,255],230*4],[[255,255,0],230*5],[[255,0,0],230*6],[[0,0,0],230*7]])
#FIRE = palette([[[0,0,0],75*1],[[255,0,0],75*1],[[255,255,0],75*1],[[255,255,255],75*1],[[255,255,0],75*1],[[255,0,0],75*1],[[0,0,0],75*1]])
custom = palette([[[124,0,33],230*1],[[55,255,180],230*2],[[5,25,255],230*3],[[0,255,255],230*4],[[255,0,33],230*5],[[255,0,0],230*6],[[0,0,0],230*7]])
greyscale = palette([[(0,0,0),75],[(255,255,255),75*2],[(0,0,0),75*3],[(255,255,255),75*4],[(0,0,0),75*5],[(255,255,255),75*6],[(0,0,0),75*7],[(255,255,255),75*8],[(0,0,0),75*9],[(255,255,255),75*10],[(0,0,0),75*12],[(255,255,255),75*13],[(0,0,0),75*14],[(255,255,255),75*15],[(0,0,0),75*16],[(255,255,255),75*17],[(0,0,0),75*18],[(255,255,255),75*19],[(0,0,0),75*20]])
pal = "grey"

def draw(pixAr,iteration_field):
    for x in range(iteration_field.shape[0]):
        for y in range(iteration_field.shape[1]):
            if pal == "grey":
                pixAr[x][y] = (greyscale[iteration_field[x][y]])
            elif pal == "fire":
                pixAr[x][y] = (FIRE[iteration_field[x][y]])





def set_lim():
    while True:
        global limit
        global pal
        u_input = input("new lim:")
        if u_input == "fire":
            pal = "fire"
        elif u_input == "grey":
            pal = "grey"
        iteration_field = fractal_engine.iterate_field(number_field,limit)
        draw(pixAr,iteration_field)
        try:  
            if int(u_input) > 0 and int(u_input)<1300:
                limit = int(u_input)
                iteration_field = fractal_engine.iterate_field(number_field,limit)
                with ThreadPoolExecutor(6) as ex:
                    ex.submit(draw(pixAr,iteration_field))
        except:
            print("changing shit")
            
        
        
    

def imag_to_coord(num_i,top_left_coordinate,bot_right_coordinate,step_r,step_i):
    mid_point_coordinate = (top_left_coordinate + bot_right_coordinate)/2
    
    x = -(mid_point_coordinate.real - num_i.real)
    x = x/step_r
    
    y = -(mid_point_coordinate.imag - num_i.imag)
    y = y/step_i
    
    return(x+width/2,y+height/2)
    
    

pygame.init()
clock = pygame.time.Clock()

top_left = -2+1.5j
#top_left = 0.25 + 0.05j
bot_right = 1-1.5j
#bot_right = 0.3 - 0.05j

mid_point = (top_left + bot_right)/2
#bot_right = 0

width = 600
height = 600


step_r = bot_right.real - top_left.real
step_r = step_r / width

step_i = bot_right.imag - top_left.imag
step_i = step_i / height

limit = 100
zoom = 1
screen = pygame.display.set_mode([width, height])
screen.fill((0, 0, 0))

pixAr = pygame.PixelArray(screen)

drag = False

number_field = fractal_engine.init_num_space(top_left,bot_right,width,height)
iteration_field = fractal_engine.iterate_field(number_field,limit/zoom)

iter_thread = threading.Thread(target = set_lim)


print_time = True

start = time.time()
number_field = fractal_engine.init_num_space(top_left,bot_right,width,height)
iteration_field = fractal_engine.iterate_field(number_field,limit/zoom)
with ThreadPoolExecutor(6) as ex:
    ex.submit(draw(pixAr,iteration_field))
    
end = time.time()
if print_time:
    print(end - start)

running = 1

iter_thread.start()

while running:
    
    clock.tick(60)
    d_r, d_i = pygame.mouse.get_rel()
    #d_r = (d_r - 250)
    #d_i = (d_i -250)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #if(drag):
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drag = True
                            
            if event.button == 3:
                print(zoom)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print_time = not print_time
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drag = False
                
                start = time.time()
                with ThreadPoolExecutor(6) as ex:
                    ex.submit(draw(pixAr,iteration_field))
                
                end = time.time()
                if print_time:
                    print(end - start)   
        elif event.type == pygame.MOUSEMOTION:
            if drag:  
                top_left -= d_r*step_r/zoom
                top_left -= d_i*step_i*1j/zoom
                bot_right -= d_r*step_r/zoom
                bot_right -= d_i*step_i*1j/zoom
                mid_point -= d_r*step_r/zoom
                mid_point -= d_i*step_i*1j/zoom
                
                number_field = fractal_engine.init_num_space(top_left,bot_right,width,height)
                iteration_field = fractal_engine.iterate_field(number_field,limit*0.67)
                start = time.time()
                with ThreadPoolExecutor(6) as ex:
                    ex.submit(draw(pixAr,iteration_field))
                
                end = time.time()
                if print_time:
                    print(end - start)
                
        elif event.type == pygame.MOUSEWHEEL:
            
            if zoom >= 0.355 and event.y < 0:  
                zoom = zoom * 1.05**event.y
                
            elif event.y > 0:
                zoom = zoom * 1.05**event.y
                
                
            bot_right = mid_point +(1/zoom-(1/zoom)*1j)
            top_left = mid_point +(-1/zoom+(1/zoom)*1j)
            number_field = fractal_engine.init_num_space(top_left,bot_right,width,height)
            iteration_field = fractal_engine.iterate_field(number_field,limit)
            start = time.time()
            with ThreadPoolExecutor(6) as ex:
                ex.submit(draw(pixAr,iteration_field))
            
            end = time.time()
            if print_time:
                print(end - start)
            
   
    pygame.draw.line(screen, (255,255,255), (295,300),(305,300), 3)
    pygame.draw.line(screen, (255,255,255), (300,295),(300,305), 3)
    
    
    pygame.display.update()
    

pygame.quit()


