# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:51:52 2020

@author: ANA
"""
import math as m

def f(x):
    return m.exp(x) - x - 5

def df(x):
    return m.exp(x) - 1

def g(x):
    return m.log(5+x,m.e)

def dg(x):
    return 1/(x+5)

print("Newton: ")
def newton(x, max_iter):
	for i in range(max_iter):
		x = x - (f(x)/df(x))
		print (i,x)
        
newton(3.0,10)
print("")

print("Picard-Peano: ")
def picard_peano(guess,max_iter):
    for i in range(max_iter):
        xn=g(guess)
        print(i, xn)
        guess = xn

picard_peano(3.0,10)