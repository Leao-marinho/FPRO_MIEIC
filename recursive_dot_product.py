# -*- coding: utf-8 -*-
"""
3. Recursive dot product

Write a function recursive_dot(l1, l2) that computes the inner dot product 
using the two lists provided — the two lists follow the same structure. 
For example, if l1=[1, [2, 3]] and l2=[4, [5, 6]], 
then the result will be 1*4+(2*5+3*6).

You might want to use type(x) to find the type of x.

For example:
● recursive_dot([1, [2, 3]], [4, [5, 6]]) 
    returns the integer 32
● recursive_dot([[5, 3, 1], [2, 4]], [[4, 2, 0], [1, 3]]) 
    returns the integer 40
● recursive_dot([2], [1]) 
    returns the integer 2
    
@author: Luísa Maria
"""

def recursive_dot(l1, l2):
    sum_ = 0
    for i in range(0, len(l1)):
        if(type(l1[i]) == list):
            sum_ = sum_ + recursive_dot(l1[i],l2[i])
        else:
            sum_ = sum_ + (l1[i] * l2[i])
            
    return sum_
        
