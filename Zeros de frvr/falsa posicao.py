# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:22:16 2020

@author: ANA
"""
def f(x):
    return 2*x**2-5*x-3

def falsa_posicao(a,b,numItr): 
	for i in range(numItr):
		x = (a*f(b)-f(a)*b)/(f(b) - f(a))
		if (f(x)*f(a)< 0):
			b = x
		else:
			a = x

		print(a,f(a),b,f(b),x)