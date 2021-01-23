import math
# Returns a dictionary containing all possible Yahtzee scores for the given dice.
def calculate_score(dice):
    dictionary = {}
    dice.sort()
    #Number count
    dict1 = dict.fromkeys(dice)
    lst = []
    for number in dict1:
        lst.append(number)
        dictionary[(str(number)+'s')] = (dice.count(number)*number)    
    #Three of a kind
    if dice.count(dice[0]) >= 3 or dice.count(dice[1]) >= 3 or dice.count(dice[2]) >= 3:
        dictionary["3 of a kind"] = sum(dice)
    #Four of a kind
    if dice.count(dice[0]) >= 4 or dice.count(dice[4]) >= 4:
        dictionary["4 of a kind"] = sum(dice)
    #Full House
    if (dice.count(dice[0]) == len(dice)-2 and dice.count(dice[4]) == len(dice)-3) or (dice.count(dice[4]) == len(dice)-2 and dice.count(dice[0]) == len(dice)-3):
        dictionary["full house"] = 25
    #Low Straight
    if (len(lst) == 4 and lst[0] == lst[1]-1 == lst[2]-2 == lst[3]-3) or (len(lst)==5 and lst[1] == lst[2]-1 == lst[3]-2 == lst[4]-3) or (len(lst)==5 and lst[0] == lst[1]-1 == lst[2]-2 == lst[3]-3):
        dictionary["low straight"] = 30
    #High straight
    if (len(lst) == 5 and (lst[0] == lst[1]-1 == lst[2]-2 == lst[3]-3 == lst[4]-4)):
        dictionary["high straight"] = 40
    #Yahtzee
    if dice.count(dice[0]) == len(dice):
        dictionary["yahtzee"] = 50
    #Chance
    dictionary["chance"] = sum(dice)   
    print(dictionary)
    return dictionary


dice = [1,2,3,4,6]

calculate_score(dice)
