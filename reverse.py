num = int(input("Number: "))

result = 0

count = 0

n = num

while(n > 0):
    n = n // 10
    count = count + 1

while(num > 0):
    d = num % 10
    num = num // 10
    result = result + (d * (10**(count-1)))
    count = count - 1
    
print(result) 