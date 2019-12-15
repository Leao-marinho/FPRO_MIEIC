"""
 5. Longest common prefix

Write a Python function longest_prefix(words) 
that given a list of words called words, 
returns the longest common prefix to all the words.

For example, if words = ["apple", "apply", "ape", "april"], 
then the biggest prefix is "ap".

You should use the divide and conquer strategy to find out the longest prefix.

@author: Luisa Maria Mesquita
"""

def longest_prefix(words):
    
    if(len(words) == 1):
        return words[0]
    
    first_elem = words[0]
    prefixes = []
    
    for i in range(1, len(words)):
        astring = ""
        if(len(words[i]) > len(first_elem)):
            for j in range(0, len(first_elem)):
                if(words[i][j] == first_elem[j]):
                    astring = astring + words[i][j]
                else:
                    break
            prefixes.append(astring)
        else:
            for j in range(0, len(words[i])):
                if(words[i][j] == first_elem[j]):
                    astring = astring + words[i][j]
                else:
                    break
            prefixes.append(astring)
        first_elem = words[i]
        
    return longest_prefix(prefixes)
                    
