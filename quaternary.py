quat = int(input("Quaternary: "))

sum_r = 0

position = 0

while(quat > 0):
    aux = quat % 10
    
    sum_r = sum_r + (aux * (4 ** position))
    
    position = position + 1
    
    quat = quat // 10
    
print(sum_r)