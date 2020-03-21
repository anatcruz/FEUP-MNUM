# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:45:59 2020

@author: ANA
"""
import math as m

def g(x):
    return -x + 40*m.cos(m.sqrt(x)) + 3

def dg(x):
    return (-20*m.sin(m.sqrt(x)))/m.sqrt(x) - 1

def newton(x, max_iter):
    print(x,g(x))
    for i in range(max_iter):
        x = x - (g(x)/dg(x))
        print (x,g(x))
        
print(newton(1.7000,2))