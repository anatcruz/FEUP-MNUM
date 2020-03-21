# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:55:21 2020

@author: ANA
"""
import math as m

def f(x):
    return m.exp(x) - 4*x**2

def g(x):
    return 2*m.log(2*x,m.e)


def picard_peano(guess,max_iter):
    for i in range(max_iter):
        xn=g(guess)
        print(i, xn)
        guess = xn
        
print(picard_peano(1.1,1))