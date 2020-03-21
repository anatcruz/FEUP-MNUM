# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:37:38 2020

@author: ANA
"""
import math as m

def f(x,y):
    return m.sin(x)

def runge_kutta(x,y,xf,h):
    while(x < xf):
        y += h * f(x + h / 2, y + (h / 2) * f(x, y))
        x += h
    print("x:",x)
    return y

r1 = runge_kutta(0,0,6,2*m.pi/20)
r2 = runge_kutta(0,0,6,2*m.pi/40)
r3 = runge_kutta(0,0,6,2*m.pi/80)

print("y1:",r1)
print("y2:",r2)
print("y3:",r3)
quociente = (r2 - r1)/(r3-r2)           
erro = (r3-r2)/3
print("quociente", quociente) 
print("erro:", erro)
