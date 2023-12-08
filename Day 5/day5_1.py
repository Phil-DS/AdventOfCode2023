
def genMap(destStart, srcStart, span):
    def f(v):
        if v < srcStart:
            return None
        
        delta = v - srcStart
        if delta >= span:
            return None
        
        return destStart + delta
    return f

def nextMapping(nextValues, maps):
    possibleMappedValues = [*nextValues]
    for i,n in enumerate(nextValues):
        for m in maps:
            mappedVal = m(n)
            if mappedVal:
                possibleMappedValues[i] = mappedVal
                break
    return [*possibleMappedValues]

with open('Day 5/day5.txt') as file:
    first = file.readline()
    # seeds = [int(v) for v in first.split()[1:]
    seeds = []
    seedOptions = first.split()[1:]
    for i in range(len(seedOptions)//2):
        if i:
            seeds.extend(range(int(seedOptions[2*i]),int(seedOptions[2*i])+int(seedOptions[(2*i)+1])))
        # break

    maps = []

    file.readline()

    nextValues = [*seeds]
    print(seeds)

    for l in file:
        l = l.strip()
        if not len(l):
            #reached end
            
            nextValues = nextMapping(nextValues, maps)
            print(nextValues)
            maps = []
            continue

        if l[0] not in '1234567890':
            continue
        
        m = tuple(map(int,l.split()))
        # print(m)
        maps.append(genMap(*m))
    nextValues = nextMapping(nextValues, maps)
    print(nextValues)
    print(min(nextValues))