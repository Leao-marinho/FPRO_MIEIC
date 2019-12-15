"""
 4. Function root 

You are given a function f: ℝ → ℝ which maps a number into another number. 
This function is convex and is defined in the interval [0, 1]. 

You will find the root (zero) of the function by using the Bisection method 
(a type of binary search).

1. Define the lower and upper bound variables as 0 and 1, respectively
2. Evaluate the function at the midpoint between the lower and upper bound
3. If f(lower) and f(midpoint) have the same sign, then lower := midpoint
4. Otherwise, upper := midpoint
5. Go back to 2 until n steps are performed
6. Return midpoint rounded to 5 digits.

Write a Python function called bisect(f, n) that, 
given a function f and steps n, returns the root approximation at that step.

Example:
    Input: lambda x: (1-(x+0.2))*(x+0.2), 10 	
    Output: 0.7998
    
@author: Luisa Maria Mesquita
"""
def bisect(f, n):
    midpoint = 0
    a = 0
    b = 1
    
    for i in range(0, n, 1):
        #mid-point of interval [0,1]
        midpoint = (a + b) / 2.0
        
        if(f(a) * f(midpoint) >= 0):
            a = midpoint
        else:
            b = midpoint
    
    return round(midpoint, 5)
