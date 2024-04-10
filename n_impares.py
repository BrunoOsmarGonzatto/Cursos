# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
import math

num = math.fabs(int(input("Digite o valor de n: ")))
i=0
x=0

while i != num:
    impar = 1 + x
    x += 2
    i += 1
    print(impar)