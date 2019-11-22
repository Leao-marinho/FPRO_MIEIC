# -*- coding: utf-8 -*-
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
    Input: (0, 0), 'up-up-left-right-up-up'
    Output:	(0, 4)

@author: Luísa Maria
"""

def map(pos, steps):
    list_steps = steps.split('-') 
    
    x = pos[0]
    y = pos[1]
    
    for i in list_steps:
        if(i == "up"):
            y = y + 1
        elif(i == "down"):
            y = y - 1
        elif(i == "right"):
            x = x + 1
        elif(i == "left"):
            x = x - 1
    
    return (x, y)
