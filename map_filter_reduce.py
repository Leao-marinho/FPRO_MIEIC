"""
Map, Filter & Reduce 

Write a function map_filter_reduce(lst, f1, f2, f3) 
that receives a list lst and three functions: f1, f2 and f3. 
The function filters the elements of lst using f1, 
applies f2 to each element of the result, 
and finally applies reduce() to convert the list to a scalar by using f3.

Example:
    Input: [1, 2, 3, 4, 5, 6, 7, 8], 
            lambda i: i % 2 == 0, 
            lambda i: i**2, 
            lambda a, b: a+b	
            
    Ouput: 120

@author: Luísa Maria Mesquita
"""
import functools

def map_filter_reduce(lst, f1, f2, f3):
    lst = list(filter(f1, lst))
    lst = list(map(f2, lst))
    lst = functools.reduce(f3, lst)
    
    return lst