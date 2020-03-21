# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:24:25 2020

@author: ANA
"""

def f(x):
    return 2*x**2-5*x-3
    
#Expressao da funcao em ordem a x
def g(x):
    return 0.4*x**2-0.6

def picard_peano(guess,max_iter,p):
    for i in range(max_iter):
        xn=g(guess)
        print(xn)
        if abs(xn-guess)<p:
            return (xn,i)
        guess = xn