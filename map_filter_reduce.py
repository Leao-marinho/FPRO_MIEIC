"""
 5. Map, Filter & Reduce

Write a function reduce_map_filter(args) 
that receives a collection of arguments called args 
and returns the result of processing args. 
This args can be either a list of integers or a tuple of type (op, f, args), 
where op is an operator ("map", "filter" or "reduce"), 
f is a function and args is again a list of integers or a tuple. 
Each function f must be applied in a chain according to the op operator.

Example:
    Input: ('map', lambda x: 2*x, [1, 2, 3]) 	
    Output: [2, 4, 6]

@author: Luísa Maria Mesquita
"""
import functools

def reduce_map_filter(args): 
    args = list(args)
    while(type(args[-1]) == tuple):
        alist = reduce_map_filter(args[-1])
        args[-1] = alist
            
    if(type(args[-1]) == list):
        alist = args[-1]
        
        if(args[0] == "map"):
            alist = list(map(args[1], alist))
        elif(args[0] == "filter"):
            alist = list(filter(args[1], alist))
        elif(args[0] == "reduce"):
            alist = functools.reduce(args[1], alist)
            
    return alist
        
        