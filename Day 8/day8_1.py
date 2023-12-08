from itertools import cycle



with open('Day 8/day8.txt') as file:
    route = cycle(file.readline().strip())
    file.readline()
    
    options = {}
    for line in file:
        options[line[:3]] = (line[7:10], line[12:15])
    
    count = 0
    base = 'AAA'
    for d in route:
        print(base, d)
        count += 1
        base = options[base][0 if d == 'L' else 1]



        if base == 'ZZZ':
            print(count)
            break