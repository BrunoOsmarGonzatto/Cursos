# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
def maior_primo(num):
    import math
    
    num = math.fabs(num)
    i = 2
    
    while num > i:
        primo = num % i 
        if primo != 0:
            i += 1
        else:
            num -= 1
            i = 2
    
    return int(num)