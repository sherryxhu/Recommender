'''
Created on Apr 25, 2018

@author: Sherry Hu
'''
import MovieReader
import RecommenderEngine 
import operator

def makerecs(name,items,ratings,size,top):
    movies = []
    top5seen = []
    top5notseen = []
    
    bestups = RecommenderEngine.recommendations(name, items, ratings, size)

    f = open("data/movies.txt")
    for line in f:
        data = line.strip().split(",")
        if data[0] == name:
            movies.append(data[1])
             
    for tup in bestups: 
        if tup[0] in movies:
            top5seen.append(tup)
    
    top5seen = [top5seen[x][0] for x in range(top)]
    
    for tup in bestups: 
        if tup[0] not in movies:
            top5notseen.append(tup)
    
    top5notseen = [top5notseen[x][0] for x in range(top)]
    
    return top5seen, top5notseen
    
if __name__ == '__main__':  
    (items, ratings) = MovieReader.getdata("data/movies.txt")
    size = len(ratings) - 1
    makerecs("student1001", items, ratings, size, 5)