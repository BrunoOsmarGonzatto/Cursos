# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
def maximo(x,y,z):
    if x >= y and x >= z:
        return x
    else:
        if y >= x and y >= z:
            return y
        else:
            return z