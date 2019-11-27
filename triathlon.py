tS = float(input("Time S: "))
tC = float(input("Time C: "))
tR = float(input("Time R: "))

result = ""

if ((tS + tC + tR) > 4):
     result = "Time"   
elif(tS > 0.75):
    result = "Swimming"
elif(tC > 2.0):
    result = "Cycling"
elif(tR > 1.25):
    result = "Running"
else:
    result = tS + tC + tR
    
    
print(result)