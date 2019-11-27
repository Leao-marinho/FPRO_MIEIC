"""
Fetching the middle

Write a Python function fetch_middle(llists) that, given a list of lists llists, 
returns a new list containing the middle element from each list in llists. 
If the list's length is even, consider the middle element to be the average 
between its two central elements (i.e. for the list [1, 2, 3, 4], 
the middle element would be (2+3)/2 = 2.5).

Example:
    Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]	
    Output: [2, 5, 8.5]

@author: Luísa Maria
"""
def is_even(num):
    if(num % 2 == 0):
        return True
    return False
    
def average_central_elements(alist):
    sum_ = alist[int(len(alist)/2) - 1] + alist[int(len(alist)/2)]
    return sum_/2
 
def middle(alist) :
    return alist[int(len(alist)/2)]     
    
def fetch_middle(llists):
    result = llists.copy()
    where = 0
    for alist in llists:
        if(is_even(len(alist))):
            result[where] = average_central_elements(alist)
            where = where + 1
        else:
            result[where] = middle(alist)
            where = where + 1
    
    return result
    
