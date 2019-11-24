"""
Biggest Member

Define a function biggest_member(atuple) that given a tuple atuple, 
returns the member of the tuple or any sub-tuple which is the biggest (in length). 
You should not care about ties.

Example:
    Input: (5, (2, 3, 1))	
    Output: (2, 3, 1)

@author: Luísa Maria
"""
def there_is_tuple(atuple):
    for elem in atuple:
        if(type(elem) == tuple):
            return True
    return False
    
def biggest_member(atuple):
    for elem in atuple:
        if(type(elem) == tuple):
            biggest = elem
            if(there_is_tuple(elem)):
                if(len(biggest_member(elem)) > len(biggest)):
                    biggest = biggest_member(elem)
            else:
                biggest = elem
        else:
            biggest = atuple

    return biggest