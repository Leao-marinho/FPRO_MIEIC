"""
2. Polynomials

Suppose we have a polynomial a represented as a list of coefficients, 
a[0], a[1], ..., a[n-1],
where a[i] is the coefficient of xi; that is:

f(x) = a0x^0 + a1x^1 + ... + anx^n

Write a function evaluate(a, x) that evaluates the value 
of the polynomial for a given integer x.

For example:
● evaluate([1, 2, 4], 5) returns the integer 111
● evaluate([1, 2, 4], 10) returns the integer 421
● evaluate([1, 2, 4, 6, 8], 2) returns the integer 197

@author: Luísa Maria
"""
def evaluate(a, x):
    sum_ = 0
    
    for i in range(0, len(a)):
        sum_ = sum_ + (a[i] * (x ** i))
        
    return sum_
    
