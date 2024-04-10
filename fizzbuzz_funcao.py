# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:10:55 2024

@author: bruno
"""
def fizzbuzz (num):
    if num % 5 == 0 and num % 3 == 0:
        return ("FizzBuzz")
    else:
        if num % 3 == 0:
            return("Fizz")
        else:
            if num % 5 == 0:
                return("Buzz")
            else:
                return(num)
        