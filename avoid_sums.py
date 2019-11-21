"""
Avoid sums

Ask the user for two numbers. 
Then add these two numbers together and print the result. 
You have to do this without using the + operator.

Hint: to ask the user for a number, you can do a = int(input()).

@author: Luísa Maria
"""

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

numbers = [num1, num2]

numbersSum = sum(numbers)

print (numbersSum)
