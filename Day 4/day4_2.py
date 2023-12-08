
from collections import defaultdict


with open('Day 4/day4.txt') as file:
    cardCount = defaultdict(lambda: 0)

    for i,card in enumerate(file):
        count = 0
        cardCount[i] += 1

        matches, numbers = tuple(card.split(':')[1].split('|'))
        matches = matches.strip().split()
        numbers = numbers.strip().split()

        for number in numbers:
            if number in matches:
                count += 1
        for c in range(count):
            cardCount[i+c+1] += cardCount[i]
            
    print(sum(cardCount.values()))