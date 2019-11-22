"""
Greatest Member

Define a function greatest_member(atuple) 
that given a tuple atuple, returns the member of the tuple 
who has the highest score; 
for tiebreakers return the member that appears first in the tuple.

The score is calculated by summing the ASCII code of each character 
for every string the member contains.

A member can be either a string or another tuple. 
In the second case, the total score of the member 
is the sum of all scores of each sub-member.

If the initial tuple has no members, return an empty tuple.

Example:
    Input: ('hyde', 'jekyll')	
    Output: 'jekyll'

@author: Luísa Maria
"""

def get_score(elem):
    atuple = ()
    if (type(elem).__name__ != 'str'):
        for e in elem:
            atuple = atuple + (get_score(e), )
            score = sum(atuple)         
    else:
        for e in elem:
            atuple = atuple + (ord(e), )
            score = sum(atuple)          
    return score

def greatest_member(atuple):
    greatest_member = atuple[0]
    biggest_score = 0
    
    for elem in atuple:
        if (int(get_score(elem)) > biggest_score):
            biggest_score = int(get_score(elem))
            greatest_member = elem
            
    return greatest_member
