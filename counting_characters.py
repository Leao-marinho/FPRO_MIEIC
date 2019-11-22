# -*- coding: utf-8 -*-
"""
Counting Characters

Write a Python function count_chars(astring) 
that returns a tuple containing the number of characters 
that are alphabetic, digits and special symbols, in the respective order.

@author: Luísa Maria
"""

import string

def count_chars(astring):
    count_alphabetic = 0
    count_digits = 0
    count_special = 0
    
    for i in astring:
        if(i in string.ascii_letters):
            count_alphabetic = count_alphabetic + 1
        elif (i in string.digits):
            count_digits = count_digits + 1
        elif (i in string.punctuation):
            count_special = count_special + 1
            
    return (count_alphabetic, count_digits, count_special)
