"""
Greatest common divisor

Write a recursive Python function gcd_rec(n1, n2) 
to find the greatest common divisor (gcd) of two integers n1 and n2.

Using global variables or cycles is forbidden.

Example:
    Input: 12, 14	
    Output: 2

@author: Luísa Maria
"""

def gcd_rec(n1, n2):
    if(n2 == 0):
        return n1
    
    elif(n1 * 5 <= n2):
        resto = n2 - (n1 * 5)
        return gcd_rec(resto, n1)
        
    elif(n1 * 4 <= n2):
        resto = n2 - (n1 * 4)
        return gcd_rec(resto, n1)
        
    elif(n1 * 3 <= n2):
        resto = n2 - (n1 * 3)
        return gcd_rec(resto, n1)
        
    elif(n1 * 2 <= n2):
        resto = n2 - (n1 * 2)
        return gcd_rec(resto, n1)
    
    elif(n1 * 1 <= n2):
        resto = n2 - (n1 * 1)
        return gcd_rec(resto, n1)
    
    else:
        return gcd_rec(0, n2)
        
    
        
