"""
5. Octal converter

Write a Python program that converts a decimal number (base 10) dec, given by user input, 
into an octal number (base 8). Decimal numbers are base 10 numbers 
and use only digits from 0 to 9, inclusive. Octal numbers can use digits from 0 to 7, inclusive.
For example:
● for dec=9, the output is the octal number 11
● for dec=64, the output is the octal number 100
● for dec=23456, the output is the octal number 55640
Save your program in the file question5.py inside the folder PE1.

@author: Luísa Maria Mesquita
"""


dec = int(input("Number: "))

result_octal = ""

while(dec > 0):
    d = dec % 8
    result_octal = str(d) + result_octal
    dec = dec // 8

print(result_octal)    
    
    
