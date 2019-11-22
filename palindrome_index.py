# -*- coding: utf-8 -*-
"""
Palindrome index

Write a Python function palindrome_index(s) that, given a string s, 
returns the index of the first character 
that, if removed, turns the string into a palindrome. 
If there is no such character or the string already is a palindrome, 
it should return -1.

Example: 
    Input: 'aaab'	
    Output: 3

@author: Luísa Maria
"""

def palindrome_index(s):
  if s[::-1] == s:
    return -1 
  
  for letter in s:
    letter_index = s.find(letter)
    
    #removes each letter until the letter removed results in a palindrome
    palindrome = s[0: letter_index] + s[letter_index + 1:]
    
  
    if palindrome[::-1] == palindrome:
      return letter_index
    
  return -1
