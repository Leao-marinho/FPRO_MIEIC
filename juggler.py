"""
Juggler Sequence

Write a recursive Python function juggler(n, p) 
that, given two integers n and p, 
calculates the p-th term in the juggler sequence for n. 
The juggler sequence for a non-negative integer n is defined as follows:

juggler(n, 0) = n
juggler(n, p) = ⌊juggler(n, p-1)^(1/2)⌋, if juggler(n, p-1) is even
juggler(n, p) = ⌊juggler(n, p-1)^(3/2)⌋, if juggler(n, p-1) is odd

Example:
    Input: 3, 1	
    Output: 5

@author: Luísa Maria
"""
def is_even(num):
    if(num % 2 == 0):
        return True
    return False
    
def juggler(n, p):
    if(p == 0):
        return n
    
    elif(is_even(juggler(n, p-1))):
        return int(juggler(n, p-1)**(1/2))
    
    elif(not is_even(juggler(n, p-1))):
        return int(juggler(n, p-1)**(3/2))
    
