"""
Pascal's triangle

Write a Python function pascal(n) that, for a given integer n, 
returns a string with the first n rows of Pascal's triangle. 
Each row finishes by "\n" (newline) and each value 
is separated by a single space. 
The value at the i-th row and j-th column of the triangle 
is equal to i!/(j!(i-j)!). 
Note that  and  start in zero. You may use math.factorial.

for the number n=3, the result is the string 1\n1 1\n1 2 1
for the number n=5, the result is the string 1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1

@author: Luísa Maria
"""

def factorial(n):
    mult = 1
    while(n > 0):
        mult = mult * n
        n = n - 1
    return mult

def pascal(n):
    result = ""
    for i in range(0, n):
        for j in range(0, i+1):
            value = factorial(i) / (factorial(j) * factorial(i - j))
            value = int(value)
            if(j > 0):
                result = result + " " + str(value)
            else:
                result = result + str(value)
            
        result = result + '\n'
          
    return result
