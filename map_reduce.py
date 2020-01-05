"""
 2. Map-Reduce

Write a Python function map_reduce(n1, n2) 
whereby you create a list of the square of the odd numbers 
between n1 and n2 ([n1, n2[). 
Then use reduce to multiply if the accumulated result 
is smaller than 50 or add the numbers otherwise. 
Ensure the result of the function is an integer.

Have a look at reduce() from module functools 
(Higher-order functions and operations on callable objects).

Example:
    Input: 0, 5 	
    Output: 9

@author: Luísa Maria Mesquita
"""
import functools

def map_reduce(n1, n2):
    alist = list(range(n1, n2))
    
    result = [i ** 2 for i in alist if (i%2 != 0)]

    f = lambda x, y: x*y if(x*y<50) else x+y
    
    return functools.reduce(f, result)

            

