# -*- coding: utf-8 -*-
"""
Counting elements

Write a function count_until(tup) that, given a tuple tup, 
returns the number of elements in it 
before an element of the type tuple appears. 
If there isn’t a nested tuple, it should return -1.

@author: Luísa Maria
"""
def count_until(tup):
    count = 0
    theres_tuple = False
    
    for i in range(0, len(tup)):
        if(type(tup[i]).__name__ == "tuple"):
            theres_tuple = True
            break
        count = count + 1
    
    if(theres_tuple == False):
        return -1
    else:   
        return count
