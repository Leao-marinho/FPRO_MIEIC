"""
Quadratic equation solver

Define a function solver(a, b, c) 
that returns the solution to the quadratic formula of the type: 
    ax²+bx+c=0. 

Return the result in the form of a list: 
    empty list if no solution exists in ℝ, 
    a list with one or two elements if one or two solutions exist, respectively; 
    if there are two solutions, use ascending order.

@author: Luísa Maria
"""

import math

def solver(a, b, c):
    
    delta = (b ** 2) - (4 * a * c)
    
    if(delta < 0):
        result = []
        
    elif (delta == 0):
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        result = [x1]
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        if(x1 < x2):
            result = [x1, x2]
        else:
            result = [x2, x1]
    
    return result
