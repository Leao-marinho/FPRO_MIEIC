"""
Rearranging 

Write a function rearrange(l) that, 
given a list of numbers l, rearranges it so that all non-positive numbers 
appear before the positive ones, but does not alter the numbers’ relative order 
(i.e., all positive numbers must appear 
in the same order relative to each other as in the original list; 
same goes for non-positive numbers).

Example:
    Input: [12, 11, -13, -5, 6, -7, 5, -3, -6, 0] 	
    Output: [-13, -5, -7, -3, -6, 0, 12, 11, 6, 5]

@author: Luisa Maria Mesquita
"""

def rearrange(l):

    negative_list = list(filter((lambda elem: elem <= 0), l))
    positive_list = list(filter((lambda elem: elem > 0), l))

    return negative_list + positive_list
            
        