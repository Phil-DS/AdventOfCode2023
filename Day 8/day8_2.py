from functools import reduce
from itertools import cycle
from math import gcd

with open('Day 8/day8.txt') as file:
    route = file.readline().strip()
    routeLen = len(route)
    file.readline()
    
    options = {}
    starts = []
    for line in file:
        options[line[:3]] = (line[7:10], line[12:15])
        if line[2] == 'A':
            starts.append(line[:3])
    
    print(starts)
    
    # count = 0

    #Find the cycles
    cycleParams = []
    zPos = {base: [] for base in starts}

    for start in starts:
        count = 0
        cycleTracker = {}
        base = start
        routeCycle = cycle(route)
        while True:
            key = (count % routeLen, base)
            cycleTrack = cycleTracker.get(key)
            if cycleTrack is not None:
                cycleLength = count - cycleTrack
                lead = cycleTrack

                print(f'{lead=} {cycleLength=}')
                cycleParams.append(cycleLength)
                break
            cycleTracker[key] = count
            if base[-1] == 'Z':
                zPos[start].append(count)
            base = options[base][0 if next(routeCycle) == 'L' else 1]
            count += 1

    s = cycleParams.pop()

    for c in cycleParams:
        s = (s*c) // gcd(s,c)

    print(s)