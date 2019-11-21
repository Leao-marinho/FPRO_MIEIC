"""
Easy change

You're helping a teller decide how to give change. 
Write a Python script that given the price of the sale 
and the amount received by user input, 
then prints a string indicating how many notes of each amount 
they have to give as change. 
Consider that the largest note available is the 50€ note 
and that all prices and amounts received are multiples of 5 (no coins!).

The result should be a string with the number of notes of each amount, 
separated by a space: "#50 #20 #10 #5".

Hint: To help format the result, use type conversions to string.

@author: Luísa Maria
"""
price = int(input("Price: "))
amount_received = int(input("Amount receveid: "))

change = amount_received - price

count_50 = 0
count_20 = 0
count_10 = 0
count_5 = 0


while(change >= 50):
    change = change - 50    
    count_50 = count_50 + 1
    
while(change >= 20):
    change = change - 20
    count_20 = count_20 + 1

while(change >= 10):
    change = change - 10
    count_10 = count_10 + 1

while(change >= 5):
    change = change - 5
    count_5 = count_5 + 1
    
print(str(count_50) + " " + str(count_20) + " " + str(count_10) + " " + str(count_5) + " ")
    
