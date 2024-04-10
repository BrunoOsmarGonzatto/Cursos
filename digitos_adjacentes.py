# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
num = int(input("Digite um número inteiro: "))

igual = False

while num != 0 and not igual:
    num_ult = num % 10
    num = num // 10
    num_ult2 = num % 10
    if num_ult == num_ult2:
        igual = True

if igual:
    print("sim")
else:
    print("não")