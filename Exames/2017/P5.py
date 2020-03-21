# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:08:22 2020

@author: ANA
"""

def w(x,y):
    return -1.1*x*y + 12*y + 7*x*x - 8*x

def dwx(x,y):
    return -1.1*y + 14*x - 8

def dwy(x,y):
    return -1.1*x + 12


def gradiente(x, y, h, numItr):
    xn = 0
    yn = 0

    for i in range(numItr):
        xn = x - h * dwx(x, y)
        yn = y - h * dwy(x, y)
        if w(xn, yn) < w(x, y):
            h *= 2
            y = yn
            x = xn

        if w(xn, yn) > w(x, y):
            h /= 2
    return w(x,y)

print("Valor da função: ",gradiente(3,1,0.1,1))

