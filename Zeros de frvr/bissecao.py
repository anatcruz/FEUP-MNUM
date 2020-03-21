# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:21:54 2020

@author: ANA
"""

def f(x):
    return 2*x**2-5*x-3

def derivada_f(x):
    return 4*x-5

#Eq que queremos resolver em ordem a x
def g(x):
    return 0.4*x**2-0.6

def derivada_g(x):
    return 0.8*x
    
def bissecao(a,b,p):
	while abs(b - a) > p :
		mid = (b + a) / 2
		if f(a) * f(mid) <= 0:
			b = mid
		else:
			a = mid
		print(a,f(a),b,f(b))
