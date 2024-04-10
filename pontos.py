# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
import math

num1 = int(input("Digite a primeira coordenada x: "))
num2 = int(input("Digite a primeira coordenada y: "))
num3 = int(input("Digite a segunda coordenada x: "))
num4 = int(input("Digite a segunda coordenada y: "))

dist = math.sqrt(((num1-num3)**2)+((num2-num4)**2))
if dist >= 10:
    print("longe")
else:
    print("perto")