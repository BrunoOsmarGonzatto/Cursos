# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
def fat (n):
   fat = 1
   while n > 1:
       fat = fat * n
       n -= 1
   return fat
        
def testa_fatorial():
    if fat(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fat(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fat(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fat(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

def binomio_newton (n,k):
    return fat(n) / (fat(k) * fat(n-k))

def bhaskara (a,b,c):

    import math
    
    delta = b**2-(4*a*c)
    
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        delta = math.sqrt(delta)
        basc_mais = (-b + delta)/(2*a)
        if delta == 0:
            print("a raiz desta equação é", basc_mais)
        else:
            basc_menos = (-b - delta)/(2*a)
            if basc_mais < basc_menos:
                print("as raízes da equação são", basc_mais, "e", basc_menos)
            else:
                print("as raízes da equação são", basc_menos, "e", basc_mais)
