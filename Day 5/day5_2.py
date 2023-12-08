def mapRange(ranges, mapMaps):
    nextRanges = []
    for r in ranges:
        base, step = r
        limit = base+step
        for dest,src,span in mapMaps:
            maxRange = src+span
            if src > base:
                if src >= limit:
                    continue
                nextRanges.append((dest, (min(limit,maxRange)-src)))
            else:
                if base >= maxRange:
                    continue
                
                delta = base - src
                if limit < maxRange:
                    nextRanges.append((dest+delta, step))
                else:
                    nextRanges.append((dest+delta,(maxRange - base)))
    assert sum(map(lambda x:x[1],ranges)) == sum(map(lambda x:x[1],nextRanges)) 
            
    return nextRanges


with open('Day 5/day5.txt') as file:
    first = file.readline()
    seeds = []
    seedOptions = first.split()[1:]
    for i in range(len(seedOptions)//2):
        seeds.append((int(seedOptions[2*i]),int(seedOptions[(2*i)+1])))
        # break

    maps = []
    mapsList = []

    file.readline()

    for l in file:
        l = l.strip()
        if not len(l):
            #reached end
            maps.sort(key = lambda x:x[0])
            # fix maps with root changes
            fixedMaps = []
            base = 0
            for m in maps:
                src,dest,step = m
                if not base == src:
                    fixedMaps.append((base,base,(src-base)))
                    base = src
                fixedMaps.append(m)
                base += step
            last = fixedMaps[-1]
            fixedMaps.append((last[0]+last[2],last[0]+last[2],999999999999))   
            mapsList.append(fixedMaps)
            maps = []
            continue

        if l[0] not in '1234567890':
            continue
        
        m = tuple(map(int,l.split()))
        maps.append(m)
    maps.sort(key = lambda x:x[0])
    # fix maps with root changes
    fixedMaps = []
    base = 0
    for m in maps:
        src,dest,step = m
        if not base == src:
            fixedMaps.append((base,base,(src-base)))
            base = src
        fixedMaps.append(m)
        base += step
    last = fixedMaps[-1]
    fixedMaps.append((last[0]+last[2],last[0]+last[2],999999999999))   
    mapsList.append(fixedMaps)

    results = []
    for seed in seeds:
        v = [seed]
        for m in mapsList:
            # print(v)
            v = mapRange(v, m)
        # print(v)
        results.extend(v)
    print(min(r for r,_ in results))