"""
Polynomials 

Suppose we have a polynomial represented as a list of coefficients, 
a[0], a[1], ..., a[n-1], where a[i] is the coefficient of x**i; 
that is: 
    f(x)=a_0x^0 + a_1x^1 + (...) + a_nx^n

Write a function evaluate(a, x) that evaluates the value of the polynomial 
for a given integer x.

Use map() and lambda functions.

Example:
    Input: [1, 2, 4], 5	
    Output: 111

@author: Luísa Maria Mesquita
"""

def evaluate(a, x):
    x_list = [x**i for i in range(0, len(a))]        

    result = list(map(lambda xn,an: xn*an ,x_list,a))
    
    return sum(result)
