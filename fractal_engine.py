import time
import numpy as np
from numba  import njit,jit

top_left = -1+1j
bot_right = 1-1j

width = 10
height = 150

limit = 100

num_space = np.zeros((width,height),dtype = complex)

def f(x, y):
        return 10 * x + y
        


@njit
def iterate_field(num_space,lim):
    w, h  = num_space.shape
    iteration_field = np.zeros((w,h),dtype=np.int8)
    for i in range(w):
        for j in range(h):
            z,c = num_space[i][j] ,num_space[i][j] 
            #z,c = num_space[i][j] , -0.75838 + 0.06711j
            for iteration in range(int(lim)):
                z = z**2 + c  
                if z.real ** 2+ z.imag ** 2 > 4:
                        iteration_field[i][j] = iteration
                        
        
    return iteration_field

@njit()
def mandelbrot_iteration(z_num,lim):
    z,c = z_num,z_num
    #z,c = z_num , -0.75838 + 0.06711j
    
    
    for iteration in range(lim):
        z = z**2 + z  
        if z.real ** 2 + z.imag ** 2 > 4:
                return iteration
    
    
    return iteration
    
@njit()
def init_num_space(top_left,bot_right,width,height):
    step_r = (-top_left.real + bot_right.real)/width
    step_i = (-top_left.imag + bot_right.imag)/height
    
    num_space = np.zeros((width, height), dtype=np.clongdouble)
    
    num_space += -top_left
    
    for i in range(width):
        for j in range(height):
            num_space[i][j] = top_left + i*step_r+j*step_i*1j
    
    return num_space


if __name__ == "__main__":
    start = time.time()
    z = -0.7519+0.0546
    

    num_space = init_num_space(top_left,bot_right,width,height)
    #print(num_space)
    itr_field = iterate_field(num_space,limit)
            
    end = time.time()
    print(end - start)

