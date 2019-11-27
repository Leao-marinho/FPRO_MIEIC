"""
3. Triangle Quest

Write a Python program that for an integer n (1-9), 
given by user input, prints a numerical triangle of height n-1 
like the one below:

1
22
333
4444
55555
...

For example:
● for n=1, the output is ""
● for n=3, the output is "1\n22"
● for n=4, the output is "1\n22\n333"
● for n=6, the output is "1\n22\n333\n4444\n55555"

"""

n = int(input("Integer n (1-9): "))

result = ""
for i in range(1, n):
    print(str(i) * i)

