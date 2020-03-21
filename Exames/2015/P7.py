# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:13:06 2020

@author: ANA
"""
import math as m

def f(x):
    return x**3 - 10*m.sin(x) + 2.8

def bissecao(a,b,numItr):
	for i in range(numItr):
		mid = (b + a) / 2
		if f(a) * f(mid) <= 0:
			b = mid
		else:
			a = mid
		print(i,a,b)
        
print(bissecao(1.5,4.2,2))