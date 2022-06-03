from hashlib import new
import numpy as np
import math

# z(new) = z(old)^2 + c     z = a + bj

def z_iterate(z , c = None):

    if c == None:
        c = z

    new_z = c + z**2

    return new_z ,c

z = -1
c = -1

for i in range(20):
    z,c = z_iterate(z,c)
    print(z)
   




