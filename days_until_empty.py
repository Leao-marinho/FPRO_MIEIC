"""
 1. Days until empty 

A tank with capacity C liters is completely filled in day=0.

1. At each day i, the tank is filled with l liters of water  
-in the case of overflow, the extra water is thrown out.
2. At the end of each day i, i liters of water are consumed.

Write a function days_until_empty(C, l) 
that returns at which day the tank will become empty.

Example:
    Input: 5, 2 	
    Output: 4
    
@author: Luísa Maria Mesquita
"""

def days_until_empty(C, l):
    capacity = C
    i = 0
    while(capacity > 0):
        i = i + 1
        capacity = capacity + l
        if(capacity >= C):
            capacity = C
            capacity = capacity - i
        else:
            capacity = capacity - i
    
    return i
