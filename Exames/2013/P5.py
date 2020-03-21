# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:35:02 2020

@author: ANA
"""
import math as m

def f(x):
    return x - 3.7 + (m.cos(x + 1.2))**3

def df(x):
    return 1 - 3*m.sin(x + 1.2)*(m.cos(x + 1.2))**2

def newton(x, max_iter):
	for i in range(max_iter):
		x = x - (f(x)/df(x))
		print (i,x)
        
print(newton(3.8,1))