"""
4. Interleave Lists

Write a Python function interleave(alist1, alist2) that, 
given two lists with the same structure but not necessarily the same length, 
alist1 and alist2, which may contain other lists, 
returns a list with the interleaved elements of both alist1 and alist2. 

For example:
● interleave([1, [4,2]], [3, [7,4]]) 
    returns the list [1,3,4,7,2,4]
● interleave(['a','b','c'], [1,2,3,4,5]) 
    returns the list ['a',1,'b',2,'c',3]
● interleave([], [1,2]) 
    returns the list []
    
@author: Luísa Maria
"""

def interleave(alist1, alist2):
    result = []
    
    if(len(alist1) <= len(alist2)):
        for i in range(0, len(alist1)):
            if(type(alist1[i]) == list):
                result = result + interleave(alist1[i], alist2[i])
            else:
                result.append(alist1[i])
                result.append(alist2[i])
        return result
    else:
        for i in range(0, len(alist2)):
            if(type(alist2[i]) == list):
                result = result + interleave(alist1[i], alist2[i])
            else:
                result.append(alist1[i])
                result.append(alist2[i])
        return result
        
    
