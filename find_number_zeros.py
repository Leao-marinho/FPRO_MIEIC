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
def count_zeros(f):
    alist = f()
    xs = alist[:int(len(alist)/2)]
    ys = alist[int(len(alist)/2):]
    xi = 0
    yi = 0
    
    while True:
        if(xi >= len(xs))
    return (xs,ys)
