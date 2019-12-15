"""
 2. Catch me if you can 

Write a Python function find_me(f, limits) that, 
given a function f and a tuple limits with two integers 
representing the search limits, return how many iterations were necessary 
until the desired number was found.

The function f receives a number and returns either 
-1 (smaller) or +1 (bigger) or 0 (found). 
You must start by guessing the middle number 
(that does not count as an iteration) 
and use binary search to adjust the limits iteratively.

Example:
    Input: lambda n: -1 if n > 31 else 1 if n < 31 else 0, (0, 100) 	
    Output: 3
    
@author: Luísa Maria Mesquita
"""
def find_me(f, limits):
    i = -1
    while True:
        guess = (limits[0] + limits[1]) // 2
        i = i + 1
        if(f(guess) == -1):
            limits = (limits[0], guess)
        if(f(guess) == 0):
            return i
        if(f(guess) == 1):
            limits = (guess, limits[1])
