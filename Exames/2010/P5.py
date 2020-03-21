# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:03:03 2020

@author: ANA
"""
def z(x,y):
    return 6*x**2 - x*y + 12*y + y**2 - 8*x

def dzx(x,y):
    return 12*x - y - 8

def dzy(x,y):
    return -x + 12 + 2*y

def gradient(x, y, h, numItr):
    xn = 0
    yn = 0
    print("x: ",x)
    print("y: ",y)
    print("z(x,y): ",z(x,y))
    print("gradiente: ",dzx(x,y),";",dzy(x,y))
    print("")
    for i in range(numItr):
        xn = x - h * dzx(x, y)
        yn = y - h * dzy(x, y)
        if z(xn, yn) < z(x, y):
            h *= 2
            y = yn
            x = xn

        if z(xn, yn) > z(x, y):
            h /= 2
        print("x: ",x)
        print("y: ",y)
        print("z(x,y): ",z(x,y))
        print("")


print(gradient(0,0,0.25,1))