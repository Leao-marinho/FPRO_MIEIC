"""
5. Quaternary to decimal converter

Decimal numbers are base10 numbers that use only digits from 0 to 9, inclusive.
Quaternary numbers are base 4 numbers that use only digits 0, 1, 2 and 3.
Write a Python program that converts a quaternary number (base 4) quat, given by user input,
into the corresponding decimal number (base 10).

For example:
● for quat=123, the output is the decimal number 27
● for quat=112233, the output is the decimal number 1455
● for quat=11, the output is the decimal number 5

"""

quat = int(input("Quaternary: "))

sum_r = 0

position = 0

while(quat > 0):
    aux = quat % 10
    
    sum_r = sum_r + (aux * (4 ** position))
    
    position = position + 1
    
    quat = quat // 10
    
print(sum_r)