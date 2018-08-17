'''
Created on Apr 25, 2018

@author: Sherry Hu
'''
def getdata(filename):
    ''' returns a tuple of 2 items:
    1. list of books being rated in alpha order
    2. a dictionary of ids as keys and their ratings as values
    '''
    d = {}
     
    f = open(filename)
    for line in f:
        data = line.strip().split(",")
    
        ratingslist = [elem for elem in data if data.index(elem)%2 == 0]
        
        if ratingslist[0] not in d:
            d[ratingslist[0]] = ratingslist[1:]
        
    booklist = [elem for elem in data if data.index(elem)%2 != 0]
    return (booklist, d)

if __name__ == '__main__':
    getdata( "data/books.txt")