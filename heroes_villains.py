"""
Heroes and Villains

Write a Python function fight(heroes, villain) 
that, given a list of heroes and a villain, 
checks if the good side can prevail. 
Each hero in the list has a set of properties stored in a dictionary: 
    name, health, category and score (number of victories). 
The villain has a similar structure, but does not record his score. 
The fight occurs within the following set of restrictions:

1.The villain only fights heroes of the same category as him.
2.The villain fights the heroes in the order they appear in the list.
3.In a hero versus villain fight, the winner 
is the one with bigger health (in case of a tie, hero wins). 
If the villain wins, diminish his health by half of the hero's health.
4.The fight ends when the villain dies or there are no more heroes.

The function should return a properly formatted string 
according to the fight result (hero or villain win), respectively:

<h> defeated the villain and now has a score of <s>

or

<v> prevailed with <hp>HP left

where <h> is the name of the hero that (finally) defeated the villain, 
<s> his updated score, 
<v> the name of the villain and 
<hp> his final remaining health (a decimal rounded to 1 decimal point).

For example:

 - fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, 
          {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, 
          {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, 
          {'name': 'King', 'health': 3750, 'category': 'S', 'score': 1}], 
          {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}) 
     returns the string: King defeated the villain and now has a score of 2
     
fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, 
       {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, 
       {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, 
       {'name': 'King', 'health': 2000, 'category': 'S', 'score': 1}], 
       {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}) 
    returns the string: Hero Killer prevailed with 1500.0HP left

@author: Luísa Maria
"""
def fight(heroes, villain):
    
    #cretaes a list of heroes of the same category as the villain
    heroes_in_fight = []
    for i in range(0, len(heroes)):
        if(heroes[i]["category"] == villain["category"]):
            heroes_in_fight.append(heroes[i])

    #fight
    winner = villain
    for heroe in heroes_in_fight:
        #villain dies
        if(villain["health"] <= 0):
            break
        
        #there's a tie
        elif(heroe["health"] == villain["health"]):
            winner = heroe
            heroe["score"] = heroe["score"] + 1
            
        #heroe wins
        elif(heroe["health"] > villain["health"]):
            winner = heroe
            heroe["score"] = heroe["score"] + 1
            villain["health"] = villain["health"] - heroe["health"]
            
        #villain wins
        elif(heroe["health"] < villain["health"]):
            winner = villain
            villain["health"] = villain["health"] - (heroe["health"] / 2)
       
    #returns who won the fight
    if(winner == villain):
        return "{0} prevailed with {1}HP left".format(villain["name"],round(villain["health"], 1))
    else:
        return "{0} defeated the villain and now has a score of {1}".format(winner["name"], winner["score"]) 














