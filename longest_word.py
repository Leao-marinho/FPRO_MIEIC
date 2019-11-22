"""
Longest word

Write a Python function longest(s) that, given a string s, 
returns the length of its longest word.

@author: Luísa Maria
"""

def longest(s):
    list_words = s.split()
    
    #Assume that the first word is the longest  
    count_longest_word = len(list_words[0])
    
    for i in range(1, len(list_words)):
        count_word = len(list_words[i])
        if (count_word > count_longest_word):
            count_longest_word = count_word
    
    return count_longest_word
