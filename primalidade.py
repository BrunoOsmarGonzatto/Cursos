# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
import math

num = math.fabs(int(input("Digite um número inteiro: ")))
i = -1
nao_primo = True

while nao_primo:
    i = math.fabs(i)
    i += 1
    primo = num % i
    if primo == 0 and i < num:
        print("não primo")
        nao_primo = False
    else:
        print ("primo")
        nao_primo = False