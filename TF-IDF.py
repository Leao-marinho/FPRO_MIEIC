# -*- coding: utf-8 -*-
"""
TF-IDF

Google or any other text-based search engine must have efficient ways 
of finding the relevant documents in a large corpus. 
To weight the importance of words in documents 
for search a numerical statistic, called tf-idf may be used. 
Typically, for each document, a vector is used. 
You will need to implement the following steps:

1. Build a vocabulary: create a list with all words in all documents, 
as lower-case
2. Build the text frequency vector (TF): create a dictionary where, 
for each word, specify a list of how many times it occurs for each document
3.Multiply each value in the dictionary by a factor known 
as the inverse document frequency (IDF): log(N/n), 
where N is the total number of documents and n is the number of documents 
where the word appears. Round the result to 3 digits.

The reason for the IDF step is to scale the vector so that words 
that appear often (like "the" or "and") are given a lower value 
because they are frequent not only in that document, but in all documents. 
The resulting element of each vector is its tf*idf.

Write a function called tfidf(documents) that receives a list of documents 
(as its string content) and returns a list of a dictionary 
for each document associating each word to its tf-idf vector.

For example:

tfidf(["To be or not to be", 
       "Impossible is a word to be found only in the dictionary of fools", 
       "There is nothing impossible to him who will try"]) 
    returns the list of tf-idf dictionaries: {'to': [0.0, 0.0, 0.0], 
                                              'be': [0.811, 0.405, 0.0], 
                                              'or': [1.099, 0.0, 0.0], 
                                              'not': [1.099, 0.0, 0.0], 
                                              'impossible': [0.0, 0.405, 0.405], 
                                              'is': [0.0, 0.405, 0.405], 
                                              'a': [0.0, 1.099, 0.0], 
                                              'word': [0.0, 1.099, 0.0], 
                                              'found': [0.0, 1.099, 0.0], 
                                              'only': [0.0, 1.099, 0.0], 
                                              'in': [0.0, 1.099, 0.0], 
                                              'the': [0.0, 1.099, 0.0], 
                                              'dictionary': [0.0, 1.099, 0.0], 
                                              'of': [0.0, 1.099, 0.0], 
                                              'fools': [0.0, 1.099, 0.0], 
                                              'there': [0.0, 0.0, 1.099], 
                                              'nothing': [0.0, 0.0, 1.099], 
                                              'him': [0.0, 0.0, 1.099], 
                                              'who': [0.0, 0.0, 1.099], 
                                              'will': [0.0, 0.0, 1.099], 
                                              'try': [0.0, 0.0, 1.099]}

@author: Luísa Maria
"""
import math

#multiplies each element of alist by log(N/n)
def multiply_by_log(alist, N, n):
    for i in range(0, len(alist)):
        alist[i] = round(alist[i] * math.log(N/n), 3)
        
    return alist

# calculates n, which is the number of documents where the word appears  
def count_not_0s(alist):
    count = 0
    for num in alist:
        if(num != 0):
            count = count + 1
    return count
  
#returns a list with each element being the number of times 
#that word appears in each document 
def count(word, documents, alist):
    where = 0
    for document in documents:
        count = 0
        for word_ in document.split(" "):
            if(word_.lower() == word):
                count  = count + 1
        alist[where] = count
        where = where + 1
    return alist
        

def tfidf(documents):
    
    #creates a list of words
    list_words = []
    for document in documents:
        list_words = list_words + document.split(" ")
        
    #Put all words in lower case
    for i in range(0, len(list_words)):
        list_words[i] = list_words[i].lower()
        
    words = set(list_words)
        
    #initializes the resulting dictionary
    result = {}
    new_list = []
    for j in range(0, len(documents)):
            new_list.append(0.0)
    for word in words:
        result[word] = new_list
        
    #creates the result
    for word in result.items():
        new_list = count(word[0], documents, word[1]).copy()
        result[word[0]] = new_list
        n = count_not_0s(new_list) #number of documents where the word appears 
                                   #numbers of "not zero" of new_list
        result[word[0]] = multiply_by_log(new_list, len(documents), n)
        
        
    return result
        




















