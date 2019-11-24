# -*- coding: utf-8 -*-
"""
Fibonacci numbers

Write a Python function fib(n) that returns a list 
of the first n Fibonacci numbers. 
The next number in a Fibonacci sequence 
is defined as the sum of the previous two numbers, 
and the first two numbers are defined as 0 and 1, respectively.

fib(1) should return the list: [0]
fib(5) should return the list: [0, 1, 1, 2, 3]

@author: Luísa Maria
"""

def fib(n):
    result = []
    for i in range(0, n):
        if(i == 0):
            result.append(0)
        elif(i == 1):
            result.append(1)
        elif(i == 2):
            result.append(1)
        else:
            result.append(result[-1] + result[-2])
    
    return result