"""
2. The sum of the squares

Write a Python program that, given an integer with one digit d 
and another integer num, both provided by user input in that order, 
prints the sum of the squares of the digits of num greater than d.

For example:
● for d=2 and num=135, the output is 34 (because of 3*3+5*5)
● for d=3 and num=135, the output is 25 (because of 5*5)
● for d=5 and num=135, the output is 0

"""

d = int(input("Digit: "))

num = int(input("Number: "))

sum_double = 0

while(num > 0):
    aux = num % 10
    if (aux > d):
        sum_double = sum_double + (aux*aux)
    num = num // 10
    
print(sum_double)