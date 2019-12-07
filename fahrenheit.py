"""
Fahrenheit 

Write a Python function to_fahrenheit(t) that, 
given a list t of temperatures in Celsius degrees, 
uses comprehensions to compute the corresponding Fahrenheit degrees, 
rounded to 2 decimals.

@author: Luísa Maria Mesquita
"""
def to_fahrenheit(t):
    result = [round((x * 1.8) + 32, 2) for x in t]
    
    return result
