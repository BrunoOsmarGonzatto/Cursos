# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
num = int(input("Digite um numero inteiro: "))

if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
else:
    print(num)