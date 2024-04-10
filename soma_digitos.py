# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
num = int(input("Digite um número inteiro: "))
soma = 0

while num != 0:
    ult = num  % 10
    num = num // 10
    soma = soma + ult

print(soma)