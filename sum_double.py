"""
2. The sum of the double

Write a Python program that, given an integer with one digit d and another integer num, 
both provided by the user in that order, prints the sum of the double 
of the digits of num greater than d.
For example:
● for d=3 and num=135, the output is 10 (because of 2*5)
● for d=2 and num=135, the output is 16 (because of 2*3+2*5)
● for d=3 and num=102, the output is 0
● for d=2 and num=12345, the output is 24
Save your program in the file question2.py inside the folder PE1.

@author: Luísa Maria Mesquita
"""

d = int(input("Digit: "))
num = int(input("Number: "))

sum_double = 0

while(num > 0):
    n = num % 10
    if(n > d):
        sum_double = sum_double + (2 * n) 
    num = num // 10

print(sum_double)    
