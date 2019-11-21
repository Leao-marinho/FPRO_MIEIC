"""
Trip Cost

You are budgeting for a car trip 
and need to know how much you will spend in fuel. 
Define a function trip_cost(distance, litres_100km, price) 
that given the distance to travel, distance, 
the number of litres of fuel needed to travel 100 km as litres_100km 
and the price (per litre) of fuel as price, 
returns the total cost of fuel for the trip. 
Use round with 2 decimal places.

def trip_cost(distance, litres_100km, price) 
    #my code here
    return  # FIXME
@author: Luísa Maria
"""

def trip_cost(distance, litres_100km, price):
    
    litres_needed = (distance * litres_100km) / 100
    cost = litres_needed * price
    
    return  round(cost, 2)

