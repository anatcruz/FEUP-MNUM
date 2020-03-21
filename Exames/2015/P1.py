# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:33:47 2020

@author: ANA
"""

def dT(T):
    return -0.25*(T - 37)

def Euler(t,tf,T,h):
    while (t < tf):                 
        T += h*dT(T)
        t += h
    return T

print(Euler(5,5.8,3,0.4))