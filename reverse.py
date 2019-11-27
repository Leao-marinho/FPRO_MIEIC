"""
1. Reverse integers
Write a Python program that, given an integer num by user input, 
computes its reverse (the number with the digits by the reverse order) 
and prints it.

You are not allowed to use string manipulation 
(for example string concatenation).

For example:
● for num=766, the output is 667
● for num=789, the output is 987
● for num=45654, the output is 45654
"""

num = int(input("Number: "))

result = 0

count = 0

n = num

while(n > 0):
    n = n // 10
    count = count + 1

while(num > 0):
    d = num % 10
    num = num // 10
    result = result + (d * (10**(count-1)))
    count = count - 1
    
print(result) 