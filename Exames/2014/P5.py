# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:10:28 2020

@author: ANA
"""
import math as m

def f(x):
    return 5*m.cos(x) - m.sin(x)

def aurea(x1,x2,numItr):
    razao = ((m.sqrt(5)-1)/2)**2
    x3 = 2.76393
    x4 = 3.23606
    print("x1: ",x1, "-->","f(x1): ",f(x1))
    print("x2: ",x2, "-->","f(x2): ",f(x2))
    print("x3: ",x3, "-->","f(x3): ",f(x3))
    print("x4: ",x4, "-->","f(x4): ",f(x4))
    print("")
    for i in range(numItr):
        if f(x3) < f(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + razao * (x2-x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x2 - razao * (x2-x1)
        print("x1: ",x1, "-->","f(x1): ",f(x1))
        print("x2: ",x2, "-->","f(x2): ",f(x2))
        print("x3: ",x3, "-->","f(x3): ",f(x3))
        print("x4: ",x4,"f(x4): ",f(x4))
        print("")

print(aurea(2,4,2))
print("-----")

def enquadrar_max(x1,x2):
    x3 = 2.76393
    x4 = 3.23606
    print("x2-x1: ",abs(x2-x1))
    print("x4-x3: ",abs(x4-x3))
    print("")

print(enquadrar_max(2,4))