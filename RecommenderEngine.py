'''
Created on Apr 11, 2018

@author: Sherry Hu
'''
import operator 

def averages(items,ratings):
    '''returns list of tuples where the first element is the item being rated, 
    and the second element is the average rating for all those who have rated 
    the item(float). 0 as a rating stands for not rated, and users who do not 
    rate an item are not counted in the average.'''
    d = {}
    ansr = []
    
    for num in range(len(items)):
        item = items[num]
        
        sum = 0
        count = 0
        for value in ratings.values():
            if value[num] != 0:
                sum += value[num]
                count += 1
        if count > 0:
            matched = (item, float(sum)/count)
        else:
            matched = (item, 0)
        ansr.append(matched)
        final = sorted(ansr, key=operator.itemgetter(1), reverse=True)  
    return final

def similarities(name,ratings):
    '''Returns dot products of the value of ratings[name] and all other values in
    ratings, sorted from highest to lowest'''
    ansr = []
    
    for key in ratings:
        if name == key:
            originalcompare = ratings[key]
          
    for key in ratings: 
        if name == key:
            continue 
        if name != key:
            sum = 0
            for num in range(len(ratings[key])):
                product = ratings[key][num] * originalcompare[num]
                sum += product
        ansr.append((key, sum))
    
    final = sorted(ansr, key=operator.itemgetter(1), reverse=True)
    return final  

def recommendations(name,items,ratings,size):
    '''creates new dictionary of size "size" (parameter) and calls both similarities and averages function.
    similarities function returns weighted scores whcich is used to multiply original ratings lists to create
    a new weighted ratings list. Returns weighted recommendations of things in items(parameter)'''
    d= {} 
    weightavgs = similarities(name, ratings)
    
    for x in range(size):
        tup = weightavgs[x]
        person = tup[0]
        multiplier = tup[1]
        origratings = ratings[person]
        weightedlist = [multiplier*num for num in origratings]
            
        if person not in d:
            d[person] = weightedlist
    
    ansr = averages(items,d)
    final = sorted(ansr, key=operator.itemgetter(0))
    final = sorted(final, key=operator.itemgetter(1), reverse=True)
    return final

if __name__ == '__main__':
    recommendations("Sarah Lee", ["DivinityCafe", "FarmStead", "IlForno","LoopPizzaGrill", "McDonalds", "PandaExpress",
     "Tandoor", "TheCommons", "TheSkillet"], {"Sarah Lee":[3, 3, 3, 3, 0, -3, 5, 0, -3], "Melanie":
   [5, 0, 3, 0, 1, 3, 3, 3, 1],"J J":[0, 1, 0, -1, 1, 1, 3, 0, 1], "Sly one":[5, 0, 1, 3, 0, 0, 3, 3, 3], 
  "Sung-Hoon": [0, -1, -1, 5, 1, 3, -3, 1, -3], "Nana Grace":[5, 0, 3, -5, -1, 0, 1, 3, 0], "Harry":
   [5, 3, 0, -1, -3, -5, 0, 5, 1], "Wei":[1, 1, 0, 3, -1, 0, 5, 3, 0]}, 3)