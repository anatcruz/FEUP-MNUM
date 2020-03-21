# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:39:33 2020

@author: ANA
"""
def f(x):
    return x**4 - 4*x**3 + x - 3

def g(x):
    return (4*x**3 - x  + 3)**(1/4)

def picard_peano(guess,numItr):
    for i in range(numItr):
        xn=g(guess)
        print(xn)
        guess = xn
        
print(picard_peano(3.5,2))