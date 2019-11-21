"""
Hypotenuse

Write a Python script that given the length n, by user input, 
which corresponds to two sides of a right-angled triangle, 
prints the length of the hypotenuse. 
Please use round with two decimal places.

@author: Luísa Maria
"""

n = int(input("Number: "))
h = ((n**2) + (n**2))**0.5
h = round(h, 2)
print(h)
