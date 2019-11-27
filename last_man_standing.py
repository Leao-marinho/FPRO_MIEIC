"""
Last Man Standing

In a circle of people, represented by a list of integers alist, 
a game will take place. 
Counting will start at the beginning of the list, 
and after counting a certain number of people, specified by step, 
the person where the counting stopped is out of the game.

Write a Python function last_man_standing(alist, step) 
that returns the last person left on the circle.

Example:
    Input: [3, 4, 1, 6, 2, 5, 7], 3	
    Output: 6
    
Order of elimination of people: 1, 5, 4, 2, 7, 2, 3    

@author: Luísa Maria
"""
def remove_and_extend(alist, step):
    if(len(alist) < step-1):
        resto = (step-1)-len(alist)
        elements_to_move = alist[resto:] + alist[0:resto]
    else:
        elements_to_move = alist[0:step-1]
    alist = alist + elements_to_move
    
    for i in range(0, len(elements_to_move)):
        alist.remove(alist[0])
    
    return alist
    
def last_man_standing(alist, step):
    while(len(alist) > 1):
        alist = remove_and_extend(alist, step)
        alist.remove(alist[0])
        print(alist)
        
    return alist[0]
