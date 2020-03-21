# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:35:29 2020

@author: ANA
"""
#z é a derivada de y

def dz(x,z):
    return 2 + x**2 +x*z

def RK4(n):
    h = 0.25
    t = 1
    y = 1
    z = 0
    for i in range(n):
        print("iteraçao: ",i,";","t: ",t)
        z1 = (h * z)
        dz1 = h * dz(t, z)
        z2 = (h * (z + dz1 / 2))
        dz2 = (h * (dz(t + h/2, z + dz1 / 2)))
        z3 = (h * (z + dz2 / 2))
        dz3 = (h * (dz(t + h/2, z + dz2 / 2)))
        z4 = (h * (z + dz3))
        dz4 = (h * (dz(t + h, z + dz3)))
        y += z1 / 6 + z2 / 3 + z3 / 3 + z4 / 6
        z += dz1 / 6 + dz2 / 3 + dz3 / 3 + dz4 / 6
        t += h