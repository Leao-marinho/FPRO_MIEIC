"""
Academy Awards

Write a Python function academy_awards(alist) 
which receives a list of tuples, alist, 
where each tuple holds the category 
and the corresponding winning movie 
and returns a dictionary that maps 
each movie to the number of awards that it won.

For example:

academy_awards([("Best Picture", "Moonlight"), 
                ("Best Director", "La La Land"), 
                ("Best Actor", "Manchester by the Sea"), 
                ("Best Actress", "La La Land"), 
                ("Best Supporting Actor", "Moonlight"),  
                ("Best Supporting Actress", "Fences"), 
                ("Best Original Screenplay", "Manchester by the Sea"), 
                ("Best Original Score", "La La Land")]) 
    should return the dictionary: {'Moonlight': 2, 
                                   'La La Land': 3, 
                                   'Manchester by the Sea': 2, 
                                   'Fences': 1}

@author: Luísa Maria
"""

#counts how much times element appears in movies_list
def count(element, movies_list):
    count = 0
    
    for movie in movies_list:
        if(movie == element):
            count = count + 1
    
    return count
        
def academy_awards(alist):
    dic = {}
    movies_list = []
    
    #creates list of movies 
    for i in range(0, len(alist)):
        movies_list.append(alist[i][1])
        
    #creates a dictionary with a movie as key and the number of awards as value
    for element in movies_list:
        dic[element] = count(element, movies_list)
        
        
    return dic
