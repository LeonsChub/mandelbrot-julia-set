import time
import numpy as np
from numba import njit

# mandelbrot equation {z(new) = z(old)^2 + c}    z = a + bj
@njit
def z_iterate(i_num , c ): #iterate once through the mandelbrot equation

    new_z = c + i_num**2

    return new_z ,c



@njit
def repeat_iteration(i_num,lim): #iterate many times through the mandelbrot equation (lim amount of times) and return when the iteration breaks when it breaches a distance greater than two from the origin
    z = i_num 
    constant = z

    for i in range(lim):
        z,constant = z_iterate(z,constant) #gets resulting z and pushes old constant to new function
        if (get_dist(z) > 4): # if the distance of the point from the origin is greater than 2 return where the limit "escaped" note the distance isnt squared in order to save time
            
            return i

    return i
        
@njit
def get_dist(z_num):
    x = z_num.real
    y = z_num.imag

    dist = x**2 + y **2 # break down imaginary and real part pythagorean therom  to find the distance 

    return dist
        


if __name__ == "__main__":

    start_time = time.time()
    print("STARTING TIME")

    print(repeat_iteration(1+0.25j,10000))

    total_time = time.time() - start_time
    print(str(total_time )+": SECONDS")

