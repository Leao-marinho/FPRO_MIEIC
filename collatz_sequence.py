"""
The Collatz sequence

Write a Python function collatz(n) 
that returns a comma-separated string with the Collatz sequence. 
Starting by the positive integer n, the next term of the Collatz sequence 
is obtained from the previous by: 
    (i) diving the previous term by 2, if the previous term is even; or 
    (ii) multiplying the previous term by 3 and then summing 1, 
    if the previous term is odd. The sequence ends when it reaches 1.

for the number n=3, the result is the string 3,10,5,16,8,4,2,1
for the number n=12, the result is the string 12,6,3,10,5,16,8,4,2,1

@author: Luísa Maria
"""

def is_even(n):
    return n % 2 == 0
    
def collatz(n):
    result = str(n) 
    while(n >= 2 and n != 1):
        if(is_even(n)):
            n = n // 2
            result =result + "," + str(n)
                
        else:
            n = (n * 3) + 1
            result =result + "," + str(n)
            
    return result
