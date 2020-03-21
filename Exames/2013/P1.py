# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 20:56:51 2020

@author: ANA
"""
def dz(t,z):
    return 0.5 + t**2 + t*z

print("Euler:")
def euler(n):
    h = 0.25
    t = 0
    y = 0
    z = 1
    for i in range(n):
        print("iteraçao: ",i,";","t: ",t)
        print("iteraçao: ",i,";","y: ",y)
        delta_z = dz(t,z)
        t += h
        y += h*z
        z += h*delta_z
        
print(euler(3))
print("-----")

print("RK4:")
def RK4(n):
    h = 0.25
    t = 0
    y = 0
    z = 1
    for i in range(n):
        print("iteraçao: ",i,";","t: ",t)
        print("iteraçao: ",i,";","y: ",y)
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

print(RK4(3))