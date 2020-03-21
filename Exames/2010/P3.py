# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:22:19 2020

@author: ANA
"""
import math as m

def dx(x,t):
    return m.sin(x) + m.sin(2*x)

def runge_kutta(t,tf,x,h):
    while(t < tf):
        x += h * dx(x + h / 2, x + (h / 2) * dx(x, t))
        t += h
        print("t: ",t)
        print("x:",x)
    return x

r1 = runge_kutta(1,1.5,0,0.250)
#r2 = runge_kutta(0,0,6,2*m.pi/40)
#r3 = runge_kutta(0,0,6,2*m.pi/80)
#
print("y1:",r1)
#print("y2:",r2)
#print("y3:",r3)
#quociente = (r2 - r1)/(r3-r2)           
#erro = (r3-r2)/3
#print("quociente", quociente) 
#print("erro:", erro)