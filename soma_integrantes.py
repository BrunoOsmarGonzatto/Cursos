# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""

num = int(input("Insira o numero para soma de seus integrantes: "))
soma = 0

while num != 0:
    soma = soma + (num % 10)
    num = num // 10

print ("a soma dos integrantes do numero digitado é", soma)