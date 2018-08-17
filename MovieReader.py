'''
Created on Apr 25, 2018

@author: Sherry Hu
'''
def getdata(filename):
    '''returns a tuple of 2 items:
    1. list of movies being rated in alpha order
    2. a dictionary of ids as keys and their ratings as values'''
    d= {}
    movieslist = []
    
    f = open(filename)
    for line in f:
        data = line.strip().split(",")
        movie = data[1]
        
        movieslist.append(movie)
        movieslist = sorted(set(movieslist))
    f.close()
    
    f2 = open(filename)
    for line in f2:   
        zeros = [0 for x in range(len(movieslist))]
        data2 = line.strip().split(",")
        id = data2[0]
        movie2 = data2[1]
        rate = int(data2[2])
        
        if id not in d:
            d[id] = zeros
        
        dex = movieslist.index(movie2)
        d[id][dex] = rate
        
    return (movieslist, d)
               
if __name__ == '__main__':
    getdata("data/movies.txt")