"""
Circle Area

Write a Python script that given the radius r of a circle by user input, 
prints the value of its area. 
Please use round with two decimal places. 
Consider pi = 3.14159.

@author: Luísa Maria
"""

pi = 3.14159

r = float(input("Raio: "))

area = pi * (r**2)
area = round(area,2)

print(area)
