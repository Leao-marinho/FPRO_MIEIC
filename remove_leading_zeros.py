# -*- coding: utf-8 -*-
"""
Remove leading zeros

Write a Python function remove_leading(ip) 
that, given a string with an IPv4 address ip, 
returns a new string with all leading zeros removed from ip. 
An IPv4 address is an address in the format N.N.N.N, 
where N is an integer in the interval [0, 255].

Example:
    Input:	'255.024.01.01'	
    Output: '255.24.1.1'

@author: Luísa Maria
"""

def count_zeros(elem):
    count = 0
    for i in range(0, len(elem)):
        if(elem[i] == "0"):
            count = count + 1
    
    return count;

def remove_leading(ip):
    
    list_ = ip.split(".")
    
    result = "."
    
    for i in range(0, len(list_)):
        for j in range(0, len(list_[i])):
            if(list_[i][j] == "0" and len(list_[i]) > 1):
                if(count_zeros(list_[i]) == 1):
                    list_[i] = list_[i].replace("0","", 1)
                    break;
                else:
                    list_[i] = list_[i].replace("0","", count_zeros(list_[i]) - 1)
                    break;
            else:
                break;
            
    
    result = result.join(list_)  
        
    return result