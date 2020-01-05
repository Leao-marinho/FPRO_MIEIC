"""
 1. Sort by lambda 

Write a Python function sort_by_f(alist) that, given a list alist, 
returns the list sorted using a lambda function, defined as:
    
    f(x) = 5-x if x ≥ 5, 
    x otherwise.
    
Example:
    Input: [-10, -6, 2, 5, 90] 	
    Output: [90, -10, -6, 5, 2]

@author: Luísa Maria Mesquita
"""
def sort_by_f(alist):
        
    alist.sort(key = lambda x: 5-x if x >= 5 else x, reverse = False)
    
    return alist
