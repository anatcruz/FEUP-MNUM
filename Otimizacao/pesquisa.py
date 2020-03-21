# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:44:28 2020

@author: ANA
"""
#PESQUISA UNIDIMENSIONAL

import math as m


def f(x):
    return (2 * x + 1) ** 2 - 5 * m.cos(10 * x)


# para minimo local
def pesquisa(guess, step):
    if f(guess) < f(guess + step):
        step = -step

    x0 = guess
    x1 = guess + step
    x2 = guess + 2 * step
    while f(x1) > f(x2):
        x0 = x1
        x1 = x2
        x2 = x2 + step
    print(x0, x1, x2)
    return [x0, x1, x2]
