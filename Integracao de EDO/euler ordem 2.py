# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:33:04 2020

@author: ANA
"""

def dz(t,z):
    return 0.5 + t**2 + t*z

def euler(n):
    h = 0.25
    t = 1
    y = 1
    z = 0
    print("Euler:")
    for i in range(n):
        print("iteraçao: ",i,";","t: ",t)
        print("iteraçao: ",i,";","y: ",y)
        delta_z = dz(t,z)
        t += h
        y += h*z
        z += h*delta_z
