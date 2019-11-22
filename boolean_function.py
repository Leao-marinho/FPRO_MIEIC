"""
Boolean function

Write a boolean function in Python called validate 
that validates a grade by outputting 
whether the grade is correct or incorrect. 
A grade is a number between 0 and 100.

You cannot use if.

@author: Luísa Maria
"""

def validate(grade):
    result = ((type(grade) == int) or (type(grade) == float))
    result = result and (grade >= 0) and (grade <= 100)
    
    return result
