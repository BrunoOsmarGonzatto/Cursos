# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = int(input("Digite o terceiro numero inteiro: "))

if num1 < num2 and num2 < num3:
    print("crescente")
else:
    print("não está em ordem crescente")