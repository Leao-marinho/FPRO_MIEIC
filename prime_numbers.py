"""
Prime numbers

Write a Python program that outputs all the prime numbers 
within a closed interval of numbers between lower and upper, 
given by user input.

For example:

for lower=2 and upper=23 the output is: 
    Prime numbers between 2 and 23 are: 2 3 5 7 11 13 17 19 23
    
for lower=5 and upper=27 the output is: 
    Prime numbers between 5 and 27 are: 5 7 11 13 17 19 23
    
for lower=-2 and upper=5 the output is: 
    Prime numbers between -2 and 5 are: 2 3 5

@author: Luísa Maria
"""

def is_prime(num):
    result = False
    if (num < 2):
        result = False
    elif(num == 2):
        result = True
    else:
        for i in range(2, num):
            if num % i == 0:
                result = False
                break
            else:
                result = True
                
    return result

lower = int(input("Lower: "))
upper = int(input("Upper: "))

prime_numbers = ""


for i in range(lower, upper + 1):
    if(is_prime(i)):
        prime_numbers = prime_numbers + " " + str(i)

print("Prime numbers between " + str(lower) + " and " + str(upper) + " are:" + prime_numbers)          


