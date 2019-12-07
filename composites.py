# -*- coding: utf-8 -*-
"""
Composites

Write a generator function get_composites(n) 
that yields a sequence of composite numbers in the interval [4, n].

There are two kinds of positive numbers: prime numbers and composite numbers. 
A composite number is the product of a sequence of prime numbers.

Example:
    Input: 10	
    Output: [4, 6, 8, 9, 10]

@author: Luísa Maria Mesquita
"""
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if(num%i == 0):
            return False
    return True
    
def get_composites(n):
    result = (i for i in range(4, n+1) if(not is_prime(i)))
            
    return list(result)
