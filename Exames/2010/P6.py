# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:54:09 2020

@author: ANA
"""
#a = [[0.1],[0.1],[0.1]]
#b = [[0.1,0.1,0.1],[0.1,0.1,0.1],[0.1,0.1,0.1]]
#c = [[0.552949],[-0.15347],[-0.10655]]
#d = a - b*c
#d = [[0.0707071],[0.0707071],[0.0707071]]

m = [[18,-1,1,0.0707071],[3,-5,4,0.0707071],[6,8,29,0.0707071]]

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

print(gauss(m))