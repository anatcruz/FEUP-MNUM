# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:47:59 2020

@author: ANA
"""
import math as m

def g(x):
    return 2*m.log(2*x,m.e)

def picard_peano(guess,numItr):
    for i in range(numItr):
        xn=g(guess)
        print(xn)
        guess = xn
        
print(picard_peano(0.9,1))