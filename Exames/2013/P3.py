# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:44:26 2020

@author: ANA
"""

def z(x,y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x

def dzx(x,y):
    return 6*x - y - 8

def dzy(x,y):
    return -x + 11 + 2*y

def gradiente(x, y, h, numItr):
    xn = 0
    yn = 0
    print("x: ",x)
    print("y: ",y)
    print("z: ",z(x,y))
    print("gradiente: ",dzx(x,y))
    print("-----")
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
    print("z: ",z(x,y))
    print("gradiente: ",dzx(x,y))
    print("-----")

print(gradiente(2,2,0.5,1))