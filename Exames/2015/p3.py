# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:41:37 2020

@author: ANA
"""

import copy as a

m = [[1,0.5,1/3,-1],[0.5,1/3,0.25,1],[1/3,0.25,0.1,1]]
mc = a.deepcopy(m)

r = [0,0,0]

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
    
gauss(m)