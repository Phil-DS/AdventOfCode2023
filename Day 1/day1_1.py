
with open('Day 1/day1.txt','r') as file:
    l = ([c for c in f if c in '1234567890'] for f in file)
    print(sum(int((n[0]+n[-1])) for n in l))

