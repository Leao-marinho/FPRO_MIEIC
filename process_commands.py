"""
2. Process commands

Write a Python function process(commands) that receives a list of commands 
to be processed over sets by the given order.

For example, [{1, 3, 4}, '|', {2, 5}] should be converted into {1, 2, 3, 4, 5}.

The following binary operations may be used:

"|": union
"&": intersection
"x": cartesian product
"-": except

Example:
    Input: [{1, 3, 4}, '|', {2, 5}, '&', {8, 2, 3}]	
    Output: {2, 3}

@author: Luísa Maria Mesquita 
"""
def process(commands):
    result = {}
    while(len(commands) != 1):
        if(commands[1] == "|"):
            result = commands[0].union(commands[2])
            commands[0] = result
            commands.remove(commands[1])
            commands.remove(commands[1])
        elif(commands[1] == "&"):
            result = commands[0].intersection(commands[2])
            commands[0] = result
            commands.remove(commands[1])
            commands.remove(commands[1])
        elif(commands[1] == "-"):
            result = commands[0].difference(commands[2])
            commands[0] = result
            commands.remove(commands[1])
            commands.remove(commands[1])
        elif(commands[1] == "x"):
            alist0 = list(commands[0])
            alist2 = list(commands[2])
            result = []
            for i in range(0, len(alist2)):
                for j in range(0 , len(alist0)):
                    result.append((alist0[j],alist2[i]), )
            result = set(result)
            commands[0] = result
            commands.remove(commands[1])
            commands.remove(commands[1])
            
                  
    return commands[0]
