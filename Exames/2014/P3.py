# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:51:12 2020

@author: ANA
"""


m = [[0.1,0.5,3.0,0.25,0.0],[1.2,0.2,0.25,0.2,1.0],[-1.0,0.25,0.3,2.0,2.0],[2.0,0.00001,1.0,0.4,3.0]]
m1 = [[0.1,0.5,3.0,0.25,0.283400],[1.2,0.2,0.25,0.2,0.283400],[-1.0,0.25,0.3,2.0,0.283400],[2.0,0.00001,1.0,0.4,0.283400]]

dimV = len(m)

def gauss(m):
    for diag in range(dimV):
        pivot1 = m[diag][diag]
        for col in range(dimV + 1):
            m[diag][col] /= pivot1
        for lin in range(diag + 1, dimV):
            pivot2 = m[lin][diag]
            for col in range(diag, dimV + 1):
                m[lin][col] -= m[diag][col] * pivot2
    for diag in range(dimV-1,-1,-1):
        for lin in range(diag-1,-1,-1):
            factor = m[lin][diag]
            for col in range(dimV,diag-1,-1):
                m[lin][col] -= m[diag][col] * factor
    print("m: ", m)
    print("-----")

print("b:")
print(gauss(m))
print("------")
print("c:")
#a=[[0.3],[0.3],[0.3],[0.3]]
#b=[[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3]]
#c=[[0.97263],[-3.06443],[0.32662],[1.82038]]
#m1 = a - b*c
print(gauss(m1))