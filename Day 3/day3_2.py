from collections import defaultdict
import re

notChar = '.1234567890'

def clamp(v,low,high):
    return max(min(v,high),low)

def testBounds(i, first, last, w, h, lines):
    for y in range(max(i-1,0),min(i+2,h-1)):
        for x in range(max(first-1,0),min(last+1,w-1)):
            if lines[y][x] == '*':
                return x,y
    return None

with open('Day 3/day3.txt') as file:
    lines = [*file]
    w,h = len(lines[0].strip()),len(lines)
    score = 0

    connected = defaultdict(list)

    for i,line in enumerate(lines):
        for match in re.finditer(r'\d+', line):
            first,last = match.span()
            bounds = testBounds(i,first,last,w,h,lines)
            if bounds is not None:
                connected[bounds].append(int(match.group()))
    
    for v in connected.values():
        if len(v) == 2:
            score += v[0]*v[1]
            

    print(score)
