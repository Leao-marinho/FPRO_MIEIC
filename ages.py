"""
3. Ages

Write a Python program that has two lists of equal size referenced by variables names 
(a list of strings) and ages (a list of integers), with values of your choice. 
The program prints all pairs name-age where name is from list names 
and age is from list age at the same position.
For example:
● for names = ["bart", "marie", "jo"] and ages = [23, 75, 19], the output
is bart-23 marie-75 jo-19
● for names = ["mary", "john"] and ages = [13, 95], the output is mary-13
john-95
Save your program in the file question3.py inside the folder PE1.

@author: Luísa Maria Mesquita
"""

names = ["bart", "marie", "jo"]
ages = [23, 75, 19]

for i in range(0, len(names)):
    print(names[i] + "-" + str(ages[i]))