"""
Bubble Sort 

Write a Python function called bubble_sort(alist) 
that receives a list alist and returns its sorted version.

The way this algorithm works is by comparing each element 
against its neighbor and swapping if the second is bigger than the first.

Example:
    Input: [5, 1, 2, 8, 2.5] 	
    Output: [1, 2, 2.5, 5, 8]

@author: Luisa Maria Mesquita
"""
def bubble_sort(alist):
 
    # Traverse through all array elements
    for i in range(len(alist)):
 
        # Last i elements are already in place
        for j in range(0, len(alist)-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if (alist[j] > alist[j+1]):
                alist[j], alist[j+1] = alist[j+1], alist[j]
                
    return alist