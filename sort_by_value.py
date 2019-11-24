"""
Sort by value

Write a Python function sort_by_value(dict) 
that, given a dictionary dict of colors 
(key is the color name and value is its hexadecimal value), 
returns a list of pairs ordered by color. 
Note that It is not possible to sort a dictionary, 
only to get a representation of a dictionary that is sorted.

For example:

sort_by_value({"Blue":"#0000FF", 
               "Green":"#008000", 
               "Black":"#000000", 
               "White":"#FFFFFF"}) returns the list: [("Black", "#000000"), 
                                                       ("Blue", "#0000FF"), 
                                                       ("Green", "#008000"), 
                                                       ("White", "#FFFFFF")]
                                                       
@author: Luísa Maria
"""
def sort_function(item):
    return item[1]
    
    
def sort_by_value(dict): 
    list_items = list(dict.items())
    list_items.sort(key = sort_function, reverse = False)
           
    return list_items
        
        
