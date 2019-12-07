# -*- coding: utf-8 -*-
"""
Celsius 

Write a Python function to_celsius(t) that, 
given a list t of temperatures in Fahrenheit degrees, 
uses comprehensions to compute the corresponding Celsius degrees, 
rounded to 1 decimal.

Example:
    Input: [84.56, 79.7, 81.14, 82.4, 82.04]	
    Output: [29.2, 26.5, 27.3, 28.0, 27.8]

@author: Luísa Maria Mesquita
"""

def to_celsius(t):
    result = [round(((x - 32) / 1.8),2) for x in t]
    
    return result
    