"""
Biggest Member

Define a function biggest_member(atuple) that given a tuple atuple, 
returns the member of the tuple or any sub-tuple which is the biggest (in length). 
You should not care about ties.

Example:
    Input: (5, (2, 3, 1))	
    Output: (2, 3, 1)

@author: Luísa Maria
"""

def biggest_member(atuple):
    biggest = atuple
    for elem in atuple:
        if(type(elem) == tuple):
            if(len(elem) > len(biggest)):
                biggest = biggest_member(elem)
                          
    return biggest