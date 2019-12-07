"""
Fahrenheit 

Write a Python function to_fahrenheit(t) that, 
given a list t of temperatures in Celsius degrees, 
uses map() with a lambda function to compute 
the corresponding Fahrenheit degrees, rounded to 2 decimals.

Example:
    Input: [29.2, 26.5, 27.3, 28, 27.8]	
    Output: [84.56, 79.7, 81.14, 82.4, 82.04]

@author: Luísa Maria Mesquita
"""
def to_fahrenheit(t):
    return list(map(lambda x: round((x * 1.8) + 32, 2),t))
