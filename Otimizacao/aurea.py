# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:22:39 2020

@author: ANA
"""
import math as m

#PESQUISA UNIDIMENSIONAL
#B = (m.sqrt(5)-1)/2
#A = B * B

def f(x):
    return x

def aurea(x1,x2,precisao):
    razao = ((m.sqrt(5)-1)/2)**2
    x3 = x1 + razao * (x2-x2)
    x4 = x2 - razao * (x2-x1)
    while abs(x2-x1) > precisao:
        if f(x3) < f(x4):
            x2 = x4
            x4 = x3
            f(x4) = f(x3)
            x3 = x1 + razao * (x2-x2)
        else:
            x1 = x3
            x3 = x4
            f(x3) = f(x4)
            x4 = x2 - razao * (x2-x1)
    
    return [a,b]
            