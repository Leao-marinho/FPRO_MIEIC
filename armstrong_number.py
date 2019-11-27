"""
1. Check Armstrong number

Write a Python program that checks if a number num with 3 digits, given by user input, 
is an Armstrong number or not. In an Armstrong number of 3 digits, 
the sum of the cubes of each digit is equal to the number itself.
Use Spyder3 to create a new file named question1.py in your folder named PE1.
For example:
● for num=153, the output is: True (1^3 + 5*3 + 3^3)
● for num=234, the output is: False

@author: Luísa Maria Mesquita
"""

num = int(input("Number: "))

number = num

sum_digits = 0

result = False

while(number > 0):
    n = number % 10
    n = n ** 3
    sum_digits = sum_digits + n
    number = number // 10
    
if(sum_digits == num):
    result = True
    
print(result)    
    
    
