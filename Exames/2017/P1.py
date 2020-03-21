# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:25:25 2020

@author: ANA
"""
#Desenhando o gráfico no máxima podemos ver que o mínimo se encontra no intervalo entre
#-2 e 2
#Existem vários métodos para minimizar uma função, para esta escolhi métode de Aurea

import math as m

def f(x):
    return x**2 + x**4

def aurea(x1,x2,precisao):
    razao = ((m.sqrt(5)-1)/2)**2
    x3 = x1 + razao * (x2-x2)
    x4 = x2 - razao * (x2-x1)
    while abs(x2-x1) > precisao:
        if f(x3) < f(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + razao * (x2-x2)
        else:
            x1 = x3
            x3 = x4
            x4 = x2 - razao * (x2-x1)
    
    return [x1,x2]

print("Minimo: ",aurea(-2,2,0.000000001))