# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:22:52 2020

@author: ANA
"""
def f(x):
    return 2*x**2-5*x-3

def derivada_f(x):
    return 4*x-5

def newton(x, max_iter):
	for i in range(max_iter):
		x = x - (f(x)/derivada_f(x))
		print (i,x)
        

def newton1(x, mas_iter):
    xn = 0
    while x!=xn:
        x = xn
        xn = xn - (f(xn)/derivada_f(xn))
        print(x,xn)