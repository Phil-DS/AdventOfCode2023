import re

rules = {'red': 12, 'green': 13, 'blue': 14}
regex = r'(\d*) (red|blue|green)'

score = 0

with open('Day 2/day2.txt','r') as file:
    for i,game in enumerate(file):
        score += i+1
        # rounds = game.split(':')[1].split
        for match in re.finditer(regex,game):
            x, col = match.groups()
            if(int(x)>rules[col]):
                score -= i+1
                break

print(score)
