"""
3. Histogram

Write a Python function histogram(alist, bins) 
that receives a alist of numbers and a tuple bins 
indicating how numbers should be divided in groups. 
The function returns the frequency distribution of the numbers 
according to the division by bins.
Given alist=[1, 1, 1, 4, 5, 8, 10] and bins=(0, 3, 7, 12), then there is the
following frequency distribution:
    
bins     |  frequency
---------------------
[0, 3[   |    3
[3, 7[   |    2
[7, 12[  |    2

and, therefore, the function returns the list [3, 2, 2].
Save the program in the file histogram.py

For example:
● histogram([1, 1, 1, 4, 5, 8, 10], (0, 3, 7, 12)) 
    returns the list [3, 2, 2]
    
● histogram([0, 3, 4, 7, 8, 1, 5], (0, 3, 7, 12)) 
    returns the list [2, 3, 2]
    
● histogram([3, 0, 1, 5, 3, 2], (0, 3, 6)) 
    returns the list [3, 3]
    
@author: Luísa Maria Mesquita
"""
def histogram(alist, bins):
    lb = bins[0]
    result = []
    for b in range(1, len(bins)):
        up = bins[b]
        count = 0
        for num in alist:
            if(num in list(range(lb, up))):
                count = count + 1
        result.append(count)
        lb = up
        
    return result
                
                
         
         