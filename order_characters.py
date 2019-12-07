"""
1. Order Characters

Write a Python function called reorder(ltuples) 
that receives a list ltuples of tuples. Each tuple is of the form (c, i) 
where c is a character and i is the position where it should be placed 
in the string.

For example, [('g', 3), ('d', 1), ('o', 2)] should be rewritten as "dog".

The indices are all different and cover the entire word.

Example:
    Input: [('g', 3), ('d', 1), ('o', 2)]	
    Output: 'dog'

@author: Luísa Maria Mesquita
"""
def sort_function(elem):
    return elem[1]

def reorder(ltuples):
    result = ""
    ltuples.sort(key = sort_function, reverse = False)
    
    for i in range(0, len(ltuples)):
        result = result + ltuples[i][0]
            
            
    return result
