import re

regex = r'(\d*) (red|blue|green)'

totalPower = 0

with open('Day 2/day2.txt','r') as file:
    for game in file:
        rounds = game.split(':')[1].split(';')
        cubes = {'red': 0, 'green': 0, 'blue': 0}

        for r in rounds:
            for match in re.finditer(regex,r):
                x, col = match.groups()
                cubes[col] = max(int(x),cubes[col])
        
        totalPower += cubes['red']*cubes['blue']*cubes['green']

print(totalPower)
