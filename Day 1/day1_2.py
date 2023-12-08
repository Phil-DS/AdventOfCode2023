import re

wordIndex = ['zero','one','two','three','four','five','six','seven','eight','nine']
words = r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|[0-9]))'

def convert(inp):
    c = inp.group(1)
    if c in '1234567890':
        return int(c)
    return wordIndex.index(c)

with open('Day 1/day1.txt','r') as file:
    l = ([convert(c) for c in re.finditer(words,f)] for f in file)
    print(sum(int((10*n[0]+n[-1])) for n in l))

