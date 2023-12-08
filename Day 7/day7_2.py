from functools import cmp_to_key
import math

faces ='J23456789TQKA'

def apply_joker(hand: str):
    noJ = hand.replace('J','')
    labels = set(noJ)
    jokerSymbol = (sorted(labels,key=lambda c: hand.count(c),reverse=True) or ['A'])[0]
    return noJ + jokerSymbol * (5-len(noJ))


def determine_strength(hand):
    labels = set(hand)
    highestCount = max((hand.count(c) for c in labels))

    match len(labels), highestCount:
        case 1, _:
            return 6
        case 2, 4:
            return 5
        case 2, 3:
            return 4
        case 3, 3:
            return 3
        case 3, 2:
            return 2
        case 4, _:
            return 1
        case 5, _:
            return 0
        
    raise ValueError(len(labels), highestCount)

def determine_order(hand1,hand2):
    for a,b in zip(hand1,hand2):
        if a == b:
            continue

        return faces.index(a) - faces.index(b)
    
def sortFn(hand1,hand2):
    fh1 = apply_joker(hand1[0])
    fh2 = apply_joker(hand2[0])

    a = determine_strength(fh1)
    b = determine_strength(fh2)

    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return determine_order(hand1[0],hand2[0])


with open('Day 7/day7.txt') as file:
    hands = [tuple(line.split()) for line in file]

    hands.sort(key=cmp_to_key(sortFn))  

    score = 0
    for i,(_,bid) in enumerate(hands):
        score += (i+1) * int(bid)

    print(score)
    