"""
Treasure
Write a Python function treasure(clues) that receives a dictionary of clues 
where each key is a location and each value is a clue of what 
is the next location to go. 
Start at (0,0) and return the tuple of the final location you end up with. 
Note that clues may be used only once.
For example, if clues={(0,0): (1,0), (2,1): (3,5), (1,0): (2,1)} 
then you should first go to (0,0) then (1,0) then (2,1) then (3,5) 
and then finish because there's no clue in that location. 
In this case, the function returns (3,5).

@author: Luísa Maria
"""

def treasure(clues):
    pos = (0,0)
    while(pos in clues):
        oldpos = pos
        pos = clues[pos]
        del clues[oldpos]
        
    return pos