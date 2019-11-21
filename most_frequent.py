"""
Most Frequent

Write a Python function most_frequent(alist) that, 
given a list alist of integers, using a dictionary, 
returns the most frequent element in alist. 
In case of ties, return the element with the greatest value.

most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]) 
    returns the integer: -1
    
most_frequent([-1, 111, 1, 11, -1, 11, 1, 111]) 
    returns the integer: 111

@author: Luísa Maria
"""

#returns the greatest value in a list of items
def find_greatest_value(list_items):
    greatest_value = list_items[0][0]
    for i in range(1, len(list_items)):
        if(list_items[i][0] > greatest_value):
            greatest_value = list_items[i][0]
            
    return greatest_value
    
#returns how many times elem appears in alist
def count(elem, alist):
    count = 0
    for num in alist:
        if(num == elem):
            count = count + 1
    return count
    
def most_frequent(alist):
    dic = {}
    
    #creates a dictionary with a number as key and the number of times 
    #that number appears in alist as value
    for i in range(0, len(alist)):
        dic[alist[i]] = count(alist[i], alist)
        
    #finds the most frquent number searching for the highest value 
    #and returning it's key
    list_items = list(dic.items())
    greatest_value = list_items[0][1]
    most_frequent_number = list_items[0][0]
    for i in range(1, len(list_items)):
        
        #in case of a tie, the most frequent is the one with greatest value
        if(list_items[i][1] == greatest_value):
            most_frequent_number = find_greatest_value(list_items)
            
        elif(list_items[i][1] > greatest_value):
            greatest_value = list_items[i][1]
            most_frequent_number = list_items[i][0]
        
        
    return most_frequent_number
