# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:12:17 2019

@author: ANA
"""

import copy as a

m = [[3,2,3,16],[2,5,1,15],[4,2,3,17]]

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
    print(m)
    print("-----")
    
    #residuos
    for eq in range(dimV):
        for sol in range(dimV):
            r[eq] = r[eq]+mc[eq][sol]*m[sol][dimV]
        r[eq] = mc[eq][dimV]-r[eq]
        
    print(r)