# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:09:16 2019

@author: ANA
"""
import math as m

def dy(x,y):
    return m.sin(x)

def Euler(x,y,xf,h):
    while (x < xf):                 
        y += h*dy(x,y)
        x += h
    print("x:",x)
    return y


r1 = Euler(0,0,6,2*m.pi/20)
r2 = Euler(0,0,6,2*m.pi/40)
r3 = Euler(0,0,6,2*m.pi/80)

print("y1:",r1)
print("y2:",r2)
print("y3:",r3)
quociente = (r2 - r1)/(r3-r2)           
erro = (r3-r2)
print("quociente", quociente) 
print("erro:", erro)
