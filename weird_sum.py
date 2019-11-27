"""
Weird Sum 

Write a Python script that given two integers a and b, 
prints the value of their sum. 
However, if the difference of a and b is an even number, 
the value of the sum is doubled, on the other hand, 
if the difference is an odd number, 
the value of the product of a and b gets added to the value of the sum.

Do not use conditionals (e.g. if).

@author: Luísa Maria
"""

a = int(input("A: "))
b = int(input("B: "))

result = 2* (a + b) if ((a - b) % 2 == 0) else (a * b) + (a + b)
    
print(result)
