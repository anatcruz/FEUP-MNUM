# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:19:39 2020

@author: ANA
"""

import math as m

def dC(T,C):
    return -m.exp(-0.5/(T+273))*C

def dT(T,C):
    return 30.0*m.exp(-0.5/(T+273))*C-0.5*(T-20)

print("a:")
def Euler(t,tf,T,C,h):
    while(t < tf):
        Cn = C + h*dC(T,C)
        Tn = T + h*dT(T,C)
        t += h
        C = Cn
        T = Tn
#        print("t: ",t, "-->", "C: ",C)
#        print("t: ",t, "-->", "T: ",T)
    return T

Euler(0,0.5,25.0,2.5,0.25)
print("")

print("b:")
def RungeKutta(t,tf,T,C,h):
    while(t < tf):
        d1 = h*dC(T,C)
        D1 = h*dT(T,C)
        d2 = h*dC(T+ (D1/2), C+(d1/2))
        D2 = h*dT(T+ (D1/2), C+(d1/2))
        d3 = h*dC(T+ (D2/2), C+(d2/2))
        D3 = h*dT(T+ (D2/2), C+(d2/2))
        d4 = h*dC(T+D3, C+d3)
        D4 = h*dT(T+D3, C+d3)
        
        Cn = C + (d1/6 + d2/3 + d3/3 + d4/6)
        Tn = T + (D1/6 + D2/3 + D3/3 + D4/6)
        
        C = Cn
        T = Tn
        t += h
        print("t: ",t, "-->", "C: ",C)
        print("t: ",t, "-->", "T: ",T)
        
RungeKutta(0,0.5,25.0,2.5,0.25)
print("")

print("c:")
def erroEuler(t,tf,T,C,h):
    print("h: ",h)
    e1 = Euler(t,tf,T,C,h)
    print("e1: ",e1)
    h/=2
    print("h: ",h)
    e2 = Euler(t,tf,T,C,h)
    print("e2: ",e2)
    print("h: ",h)
    h/=2
    e3 = Euler(t,tf,T,C,h)
    print("e3: ",e3)
    quociente = (e2 - e1)/(e3-e2)           
    erro = (e3-e2)
    print("quociente: ",quociente)
    print("erro: ",erro)
    
erroEuler(0,0.5,25.0,2.5,0.25)