# -*- coding: utf-8 -*-
"""
Combinations

Write a Python function C that receives the number of objects to choose from n, 
the number of objects selected r and produces all combinations possible.

Remember the formula:
     n   
    C = (n!) / (r!(n-r)!)
     r


Round the result to the floor, 
for example the floor of 8.4 is 8 and the floor of 5.7 is 5. 

You cannot use the math package.

@author: Luísa Maria
"""

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result 

def C(n, r):
    result = factorial(n) / (factorial(r) * factorial(n-r))
    return int(result) 
