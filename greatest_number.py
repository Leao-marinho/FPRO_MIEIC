# -*- coding: utf-8 -*-
"""
The greatest number

Write a Python function greatest(num) that, 
given a non-negative integer num, computes the greatest number 
that can be made using all digits of num.

@author: Luísa Maria
"""

def find_biggest(num):
    biggest_number = int(num[0])
    for i in num:
        if(int(i) > biggest_number):
            biggest_number = int(i)
    return str(biggest_number)
    
def greatest(num):
    #forms a list of digits of num
    #all elements of that list are int
    list_digits = []
    listDigits = []
    copy_num = num
    while(copy_num > 0):
        list_digits.append(copy_num%10)
        copy_num = copy_num // 10
    
    #forms a list of digits of num
    #where all elements of that list are str
    for i in range(0, len(list_digits)):
        listDigits.append(str(list_digits[i]))
     

    #finds greatest number 
    result = ""
    if(num == 0):
        return num
    
    while(num > 0):
        biggest = find_biggest(listDigits)
        result = result + str(biggest)
        num = num // 10
        listDigits.remove(biggest)
    
    return int(result)
