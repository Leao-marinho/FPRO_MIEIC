"""
Find the treasure

The path to the treasure is given as a sequence of commands 
that are steps of length 1: up, left, right or down. 

Write a function map(pos, steps) that takes a coordinate pos, 
which is a tuple with values x and y as (x,y), 
and a sequence of commands in a string steps, 
with the steps separated by a hyphen, 
and computes the final position in the map.

Example: 
    Input: (0, 0), ['up', 'up', 'left', 'right', 'up', 'up']	
    Output:(0, 4)
    
@author: Luísa Maria
"""
def map(pos, steps):
    if(steps == []):
        return pos
    
    elif(steps[0] == "up"):
        steps.remove("up")
        pos = map((pos[0], pos[1]+1), steps)
        
    elif(steps[0] == "down"):
        steps.remove("down")
        pos = map((pos[0], pos[1]-1), steps)
        
    elif(steps[0] == "right"):
        steps.remove("right")
        pos = map((pos[0]+1, pos[1]), steps)
        
    elif(steps[0] == "left"):
        steps.remove("left")
        pos = map((pos[0]-1, pos[1]), steps)
    
    return pos
        
