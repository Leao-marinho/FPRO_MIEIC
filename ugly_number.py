"""
Ugly number

Write a Python function ugly(n) 
to check whether a given positive number n is an ugly number. 
Ugly numbers are positive numbers whose prime factors 
only include 2, 3, 5. To check if a number is ugly, 
divide the number by the prime factors 2, 3 or 5, 
if the number becomes 1 then it is an ugly number, otherwise it is not. 
For example, 6, 8 are ugly while 14 is not ugly 
since it includes another prime factor 7. 
By convention, 1 is also an ugly number.

for the number n=6, the result is True
for the number n=14, the result is False

@author: Luísa Maria
"""

def ugly(n):
    
    if(n % 3 == 0):
        n = n / 3
    if(n % 5 == 0):
        n = n / 5
    if(n % 2 == 0):
        n = n / 2
        
    return n == 1
