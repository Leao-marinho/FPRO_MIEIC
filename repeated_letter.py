# -*- coding: utf-8 -*-
"""
First repeating letter

Write a Python function repeated_letter(s) 
which returns the first character to repeat itself.

Example:
    Input: 'tweet'	
    Output: 't'
    
@author: Luísa Maria
"""

def repeated_letter(s):
  
    for i in range(0, len(s)):
        for j in range(1, len(s)):
            if(j > i):
                if(s[i] == s[j]):
                    return s[i]
    return None
