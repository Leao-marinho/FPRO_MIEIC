# -*- coding: utf-8 -*-
"""
Square Root

The square root of any non-negative number 
can be calculated using the following algorithm:

1. Calculate the midpoint of the interval [a, b] of possible values 
for the square root of the number;

2. If the midpoint is the solution or the limits of the interval agree 
at least on 5 decimal places, exit the iteration 
and return the solution obtained;

3. If the midpoint is greater than the solution, 
then define it as the new upper limit of the interval, 
otherwise define it as the new lower limit of the interval;

4. Iterate this process until the condition to exit is met.

Write a Python program that receives a float n, provided by the user, and calculates the square root by implementing the algorithm described.

@author: Luísa Maria
"""
num = float(input("Number: "))

x0 = num/2

x1 = (x0 + (num // x0)) / 2 

xn = x1

while (True):   
    x_np1 = (xn + (num / xn)) / 2
    
    x_np1 = round(x_np1, 5)
    
    if(x_np1 == xn):
        print(x_np1)
        break;
        
    xn = x_np1
