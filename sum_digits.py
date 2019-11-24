# -*- coding: utf-8 -*-
"""
Sum of digits

Write a recursive Python function sum_digits_rec(n) 
that returns the sum of the digits of an integer number.

Using global variables or cycles is forbidden.

Example:
    Input: 12	
    Output: 3
    
@author: Luísa Maria
"""

def sum_digits_rec(n):
    sum_ = n % 10
    n = n // 10
    if(n % 10 != 0 or len(str(n)) > 1):
        sum_ = sum_ + sum_digits_rec(n)
        return sum_
    else:
        return sum_
