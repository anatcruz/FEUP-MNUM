# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:34:20 2020

@author: ANA
"""
import math as m

def f(x,y):
    return m.sin(x)

def runge_kutta(x,y,xf,h):
    while(x < xf):
        delta_1 = h*f(x,y);
        delta_2 = h*f(x+ (h/2), y+(delta_1/2))
        delta_3 = h*f(x+(h/2), y+(delta_2/2))
        delta_4 = h*f(x+h, y+delta_3)
        
        y += (delta_1/6) + (delta_2/3) + (delta_3/3) + (delta_4/6)
        x += h
    print("x:",x)
    return y

r1 = runge_kutta(0,0,6,2*m.pi/160)
r2 = runge_kutta(0,0,6,2*m.pi/320)
r3 = runge_kutta(0,0,6,2*m.pi/640)

print("y1:",r1)
print("y2:",r2)
print("y3:",r3)
quociente = (r2 - r1)/(r3-r2)           
erro = (r3-r2)/15
print("quociente", quociente) 
print("erro:", erro)
