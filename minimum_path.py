"""
5. Minimum path

Write a function min_path(matrix, a, b, visited=[]) 
that discovers the minimum path between a and b inside the matrix maze 
without going through visited twice. 
Positions a and b are tuples (line, column), 
matrix is a matrix of booleans with False indicating no obstacle 
and True indicating an obstacle and visited is a list of visited tuples. 
Valid movements include all 8 adjacent tiles.
For the maze of the following figure, 
a minimum path between a and b, in yellow, is 4:
    
    False      False   False    Yellow(b)
    False      True    Yellow   False
    Yellow(a)  True    Yellow   False
    False     Yellow   False    False
    
For example:
    ● mx = [
            [False]*4,
            [False, True, False, False],
            [False, True, False, False],
            [False]*4
           ]
● min_path(mx, (2, 0), (0, 3)) returns the integer 4
● min_path(mx, (3, 1), (0, 1)) returns the integer 3
● min_path(mx, (0, 0), (3, 3)) returns the integer 4

@author: Luísa Maria
"""
mx = [[False]*4,[False, True, False, False],[False, True, False, False],[False]*4]
IMPOSSIBLE = 999999
def min_path(matrix, a, b, visited=[]):
    if a == b: # final position
        return 0
    if a[0] < 0 or a[0] >= len(matrix): # outside matrix lines
        return IMPOSSIBLE
    if a[1] < 0 or a[1] >= len(matrix[0]): # outside matrix columns
        return IMPOSSIBLE
    if matrix[a[0]][a[1]]: # an obstacle
        return IMPOSSIBLE
    if a in visited: # already visited
        return IMPOSSIBLE
    
    # find a min path
    mindist = IMPOSSIBLE
    possible = [(0,1), (1,0), (1,1), (-1,-1), (-1,0), (-1,1), (0,-1), (1,-1)]
    for p in possible:
        l, c = a[0]+p[0], a[1]+p[1]
        # try the direction
        d = 1 + min_path(matrix, (l, c), b, visited+[a])
        # see if it's the best so far
        if d < mindist:
            mindist = d
    return mindist
