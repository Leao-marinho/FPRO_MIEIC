d = int(input("Digit: "))

num = int(input("Number: "))

sum_double = 0

while(num > 0):
    aux = num % 10
    if (aux > d):
        sum_double = sum_double + (aux*aux)
    num = num // 10
    
print(sum_double)