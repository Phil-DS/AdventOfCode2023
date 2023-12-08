with open('Day 4/day4.txt') as file:
    score = 0
    for card in file:
        count = 0
        matches, numbers = tuple(card.split(':')[1].split('|'))
        matches = matches.strip().split()
        numbers = numbers.strip().split()
        for number in numbers:
            if number in matches:
                count += 1
        if count:
            score += 1 << (count-1)
print(score)