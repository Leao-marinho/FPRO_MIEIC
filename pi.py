# -*- coding: utf-8 -*-
"""
π

Write a Python program that computes and prints the number pi 
by using the Ramanujan formula.

You can use the math package for the factorial and square root (only!). 
The number k controls the precision of the formula. Use k = 50. 
Round the result to 8 decimal places.

@author: Luísa Maria
"""

import math

k = 50 #precision

result_sum = 0

numerator = 9801

for i in range(0, k):
    numerator_from_sum = math.factorial(4 * i) * (1103 + 26390 * i)
    denominator_from_sum = (math.factorial(i)**4) * (396 ** (4*i))
    result_sum = result_sum + (numerator_from_sum / denominator_from_sum)

denominator = 2 * math.sqrt(2) * result_sum

pi = numerator / denominator

print(round(pi,8))
