"""
Change

Write a Python function change(money) 
that converts a given amount of money (≥ 0) 
into several Euro coins. 
Minimize the number of coins given.

The return value should be a dictionary specifying 
how many coins of each type should be given to the customer. 
The keys of the dictionary should correspond to each coin: 
    from 0.01 (1 cent) all the way up to 2.00 (2 euros).

Using if-else is forbidden.

Example:
    Input: 5
    Output: {2.0: 2, 1.0: 1, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    
@author: Luísa Maria
"""
def maior_ou_igual_que_0(money, coin):
    return money >= coin
    
def change(money):
    count2euros = 0
    count1euro = 0
    count50cents = 0
    count20cents = 0
    count10cents = 0
    count5cents = 0
    count2cents = 0
    count1cent = 0
    
    result = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}

    while(maior_ou_igual_que_0(money, 2.0)):
        count2euros = count2euros + 1
        money = round((money - 2.0),2)
    while(maior_ou_igual_que_0(money, 1.0)):
        count1euro = count1euro + 1
        money = round((money - 1.0),2)
    while(maior_ou_igual_que_0(money, 0.5)):
        count50cents = count50cents + 1
        money = round((money - 0.5),2)
    while(maior_ou_igual_que_0(money, 0.2)):
        count20cents = count20cents + 1
        money = round((money - 0.2),2)
    while(maior_ou_igual_que_0(money, 0.1)):
        count10cents = count10cents + 1
        money = round((money - 0.1),2)
    while(maior_ou_igual_que_0(money, 0.05)):
        count5cents = count5cents + 1
        money = round((money - 0.05),2)
    while(maior_ou_igual_que_0(money, 0.02)):
        count2cents = count2cents + 1
        money = round((money - 0.02),2)
    while(maior_ou_igual_que_0(money, 0.01)):
        count1cent = count1cent + 1
        money = round((money - 0.01),2)
                
                
    result[2.0] = count2euros
    result[1.0] = count1euro         
    result[0.5] = count50cents      
    result[0.2] = count20cents 
    result[0.1] = count10cents      
    result[0.05] = count5cents      
    result[0.02] = count2cents      
    result[0.01] = count1cent     
    
    return result

           
                
                