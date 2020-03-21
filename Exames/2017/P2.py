# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:29:50 2020

@author: ANA
"""
import math as m

def f(x):
    return m.exp(2.5*x)

def df(x):
    return 2.5*m.exp(2.5*x)

def l(x):
    return m.sqrt(1+(df(x))**2)

print("trapezio:")
def trapezio(a,b,h):
    n = round((a-b)/h)
    total = 0
    for i in range(1,n):
        total += 2*l(a+i*h)

    total+= l(a)+l(a+n*h) 
    total *= h/2
    
    return total

# Calculo do coeficiente de convergencia

r1 = trapezio(0,1,0.125)
r2 = trapezio(0,1,0.125/2)
r3 = trapezio(0,1,0.125/4)

coeficiente = (r2-r1)/(r3-r2) 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro absoluto estimado 

erro = (r3-r2)/3
print("erro:", abs(erro))
print("")

print("simpson")
def simpson(a,b,h):
    total = 0;
    n = round((b-a)/h)
    for i in range(1,n,2):
        total += 4*l(a+i*h)
    for i in range(2,n,2):
        total += 2*l(a+i*h)
    total += l(a) + l(a+n*h)
    total *= h/3
    
    return total
    
#Calculo do coeficiente de convergencia
r1 = simpson(0,1,0.125)
r2 = simpson(0,1,0.125/2)
r3 = simpson(0,1,0.125/4)

coeficiente = (r2-r1)/(r3-r2) 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro 

erro = (r3-r2)/15
print("erro:", abs(erro))