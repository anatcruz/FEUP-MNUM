# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:04:31 2020

@author: ANA
"""
import math as m

def f(x):
    return m.exp(1.5*x)

def simpson(a,b,h):
    total = 0;
    n = round((b-a)/h)
    for i in range(1,n,2):
        total += 4*f(a+i*h)
    for i in range(2,n,2):
        total += 2*f(a+i*h)
    total += f(a) + f(a+n*h)
    total *= h/3
    
    return total
    
#Calculo do coeficiente de convergencia
r1 = simpson(1,1.5,0.125)
r2 = simpson(1,1.5,0.125/2)
r3 = simpson(1,1.5,0.125/4)

coeficiente = (r2-r1)/(r3-r2) 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro 

erro = (r3-r2)/15
print("erro:", abs(erro))