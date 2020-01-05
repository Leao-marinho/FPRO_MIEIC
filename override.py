"""
 4. Override operation 

Write a function override(l1, l2) that, given two lists of tuples, 
performs the operation l1 ++ l2 known as override. 
The override operation, given two lists of tuples, 
produces a new list with every member of l2 and every member of l1 
that is not overridden by an element from l2 
(i.e., does not begin with the same atomic element). 

For example, 
[(a,b), (c,d), (c, e)] ++ [(a,c), (b,d)] = [(a,c), (b,d), (c,d), (c,e)]

Note that (a,b) from the first list was overridden by (a,c) 
from the second list and all others elements were maintained.

The resulting list should be ordered by the first element of each tuple.

Example:
    Input: [('z', 'x', 'y', 'w'), ('z', 'w', 'y', 'w')], 
           [('z', 'x'), ('w', 'a', 'b')] 	
    Output: [('w', 'a', 'b'), ('z', 'x')]

@author: Luísa Maria Mesquita
"""
def sort_function(atuple):
    return atuple[0]

def override(l1, l2):
    #list of letters with the first elements of each tuple of l2
    letters = list(map(lambda x: x[0], l2))
    
    #l1 elemets where their first element is not in letters
    temp = list(filter(lambda x: x[0] not in letters, l1))
    
    result = temp + l2
    result.sort(key = sort_function, reverse = False)
                
    return result

