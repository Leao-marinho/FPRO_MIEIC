# -*- coding: utf-8 -*-
"""
Find the bitonic point 

Given a list, that is partially ascending and partially descending, 
the bitonic point is the point before which the list is ascending 
and after which the list is descending. 
For example in the list alist=[2, 6, 10, 25, 60, 30, 25, 10, 0], 
the point 60 is the bitonic point.

Write a Python function bitonic_point(f) 
that receives a function f that when called 
produces a list of integers which is sorted in bitonic way. 
Take advantage of the way the list is sorted 
to reduce complexity time from O(n) to O(log n).

Adapted from: Geeks for Geeks 

Example:
    Input: lambda: [2, 6, 10, 25, 60, 30, 25, 10, 0] 	
    Output: 60

@author: Luisa Maria Mesquita
"""

def bitonic_point(f):
    alist = f()
    actual_elem = alist[0]
    for i in range(1, len(alist)):
        if (alist[i] < actual_elem):
            return actual_elem
        actual_elem = alist[i]
    