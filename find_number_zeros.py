"""
Find the number of zeros

Write a Python function count_zeros(f) 
that receives a function f that when called 
produces a list of integers alist. 

This list has several 1s followed by 0s (for example, alist=[1, 1, 1, 0, 0]). 
Your function must count the number of zeros on that list.
The naive solution would iterate through the list in O(n) time. 
Take advantage of the fact that the list is ordered to reduce 
that time to O(log n).

Adapted from: Geeks for Geeks 

Example:
    Input: lambda: [1, 1, 1, 0, 0] 	
    Output: 2
    
@author: Luisa Maria Mesquita
"""
def find_first_zero(alist, lb, ub):
    
    mid_index = (lb + ub) // 2
     
    if(alist[mid_index] == 0 and alist[mid_index-1] == 1):
        return mid_index
    
    elif(alist[mid_index] == 1):
        return find_first_zero(alist, (mid_index + 1), ub)
    
    elif(alist[mid_index] == 0 and alist[mid_index-1] == 0):
        return find_first_zero(alist, lb, (mid_index - 1))
        
    
def count_zeros(f):
    alist = f()
    
    first = find_first_zero(alist, 0, len(alist) - 1)
                 
    return (len(alist) - first)
        