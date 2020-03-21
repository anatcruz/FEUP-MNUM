# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:25:58 2020

@author: ANA
"""
import math as m

# funcoes
def f1(x, y):
    return 2 * x * x - x * y - 5 * x + 1


def f2(x, y):
    return x + 3 * m.log10(x) - y * y


def gx(x, y):  # achando a funcao de x, com f1
    return m.pow((x * y + 5 * x - 1) / 2, 1 / 2)


def gy(x, y):  # achando a funcao y, com f2
    return m.pow(x + 3 * m.log(x), 1 / 2)


# Metodo de paragem: erro absoluto
def picardPeano_2_error(x, y, erro):
    x = 1
    y = 1
    xAnt = 2
    yAnt = 2
    while (abs(xAnt - x) >= erro or abs(yAnt - y) >= erro):
        xAnt = x
        yAnt = y
        x = gx(x, y)
        y = gy(xAnt, y)


# Metodo de paragem: numero de iterações
def picardPeano_2(x, y, max_iter):
    for i in range(max_iter):
        xAnt = x
        x = gx(x, y)
        y = gy(xAnt, y)

