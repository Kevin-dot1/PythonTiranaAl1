from random import random,randrange
import math

def findSqrt(nr):
    g = round(nr/randrange(1,nr))

    while nr != g*g:
        print(g*g,(g+nr/g)/2)

        if (nr==math.ceil(g * g)):
            return g
        else:
            g=(g+nr/g)/2

findSqrt(8)
