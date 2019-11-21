"""
Multiples of 3 or 5

Define a function sum_multiples(n) 
that returns the sum of all the natural numbers 
that are a multiple of 3 or 5 up until n (inclusive).

def sum_multiples(n):
    # my code here
    return # FIXME

@author: Luísa Maria
"""

def sum_multiples(n):
    sum_n = 0
    for i in range(1, n + 1):
        if(i % 3 == 0 or i % 5 == 0):
            sum_n = sum_n + i
            
        
    return sum_n
