"""
Looping Numbers

A number is called a Looping Number if all adjacent digits in it differ by 1. 
The difference between 9 and 0 is considered as 1. 
All single digit numbers are considered looping numbers.

Write a Python program that receives an integer n, 
provided by the user, and checks whether the number is a jumping number or not. 
If the number is a looping number, print the message Looping number, 
otherwise print the message Not a looping number.

You can assume that all inputs are non-negative numbers.

@author: Luísa Maria
"""

num = int(input("Number: "))

isLooping = False

c = num % 10
num = num // 10
b = num % 10
a = num // 10

if(a == 9 and b == 0)or(a == 0 and b == 9)or(c == 9 and b == 0) or (c == 0 and b == 9):
    isLooping = True
elif(a + 1 == b and c - 1 == b):
    isLooping = True
elif(a - 1 == b and c + 1 == b):
    isLooping = True


if(isLooping):
    print("Looping number")
else:
    print("Not a looping number")

