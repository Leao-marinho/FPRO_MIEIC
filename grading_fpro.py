"""
Grading FPRO

Write a Python program that, given the four components of the FPRO grade, 
by user input, returns the student's grade, an integer from 0 to 20, 
by using the formula:

grade = (LE + RE + 5 * PE + 3 * TE) / 50

The program returns:

 - "Input error", if the any of the components is not between 0 and 100
 - "RFC", if the PE < 40 or the TE < 40
 - the grade as an integer, otherwise

@author: Luísa Maria
"""
LE = int(input("LE: "))
RE = int(input("RE: "))
PE = int(input("PE: "))
TE = int(input("TE: "))

grade = ((LE + RE + (5 * PE) + (3 * TE))) / 50

if(LE < 0 or RE < 0 or PE < 0 or TE < 0 or LE > 100 or RE > 100 or PE > 100 or TE > 100):
    print("Input error")
elif(PE < 40 or TE < 40):
    print("RFC")
else:
    if(((grade*10)%10) == 5.0):
        grade = round(grade + 0.1, 0)
        grade = int(grade)
        print(grade)
    else:
        grade = round(grade, 0)
        grade = int(grade)
        print(grade)
