# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:48:14 2020

@author: ANA
"""

#PESQUISA UNIDIMENSIONAL
#RAZAO 1/3

def f(x):
    return x

def tercos(a,b,precisao):
    razao = 1/3
    while abs(b-a) > precisao:
        c = a + razao * (b-a)
        d = b - razao * (b-a)
        
        if f(c) < f(d) :
            b = d
        else:
            a = c
    
    return [a,b]