# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
import math

def main():
    a = float(input("Insira o valor da a: "))
    b = float(input ("Insira o valor de b: "))
    c = float(input ("Insira o valor de c: "))
    raizes(a, b, c)

def delta (a,b,c):
    return b**2-(4*a*c)

def raizes (a,b,c):
    d = delta(a,b,c)
    if d < 0:
        print("esta equação não possui raízes reais")
    else:
        basc_mais = (-b + math.sqrt(d))/(2*a)
        if d == 0:
            print("a raiz desta equação é", basc_mais)
        else:
            basc_menos = (-b - math.sqrt(d))/(2*a)
            if basc_mais < basc_menos:
                print("as raízes da equação são", basc_mais, "e", basc_menos)
            else:
                print("as raízes da equação são", basc_menos, "e", basc_mais)