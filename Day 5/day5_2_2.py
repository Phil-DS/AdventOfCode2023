
def genMap(destStart, srcStart, span):
    def f(v):
        if v < srcStart:
            return None
        
        delta = v - srcStart
        if delta >= span:
            return None
        
        return destStart + delta
    return f

def nextMapping(v, maps):
    n = v
    for m in maps:
        mappedVal = m(n)
        if mappedVal:
            n = mappedVal
            break
    return n

with open('Day 5/day5.txt') as file:
    first = file.readline()
    # seeds = [int(v) for v in first.split()[1:]]
    seeds = []
    seedOptions = first.split()[1:]
    


    maps = []

    file.readline()

    nextValues = [*seeds]

    maps = []
    mapsList = []

    file.readline()

    for l in file:

        l = l.strip()
        if not len(l):
            #reached end
            # maps.sort(key = lambda x:x[0])
             
            mapsList.append(maps)
            maps = []
            continue

        if l[0] not in '1234567890':
            continue
        
        m = tuple(map(int,l.split()))
        maps.append(genMap(*m))


    best = 9999999999999999999999999999
    bestSeed = None

    stepSize = 100000

    for i in range(len(seedOptions)//2):
        start = int(seedOptions[2*i])
        length = int(seedOptions[(2*i)+1])
        for seed in range(start, start+length, stepSize):
            nv = seed
            for m in mapsList:
                nv = nextMapping(seed,m)
            if nv < best:
                best = nv
                bestSeed = (max(seed - stepSize, start), min(seed + stepSize, start+length))
                topSeed = seed
    
    # topSeed = 0
    # for i in range(3,-1,-1):
    # stepSize = 10**i
    best = 9999999999999999999999999999
    newBestSeed = None
    for seed in range(*bestSeed):
        nv = seed
        for m in mapsList:
            nv = nextMapping(seed,m)
        if nv < best:
            best = nv
            topSeed = seed
            newBestSeed = (max(seed - stepSize, int(seedOptions[2*i])), max(seed + stepSize, int(seedOptions[2*i]) +int(seedOptions[(2*i)+1])))
    bestSeed = newBestSeed

    print(best)