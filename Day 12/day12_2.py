from collections import defaultdict
from itertools import permutations


def matchstring(test,springs):
    return all(a==b or b=='?' for a,b in zip(test,springs))

# def search(key, springs):
#     print(springs, len(springs) - (sum(key)+max(0,len(key)-1)))

def searchString(key,springs):
    cstates = defaultdict(lambda: 0)
    nstates = defaultdict(lambda: 0)
    
    cstates[(0,0,0,0)]= 1

    score = 0
    springLen = len(springs)
    keyLen = len(key)
    while len(cstates):
        for (springIndex,keyIndex,cc,expectWorking), num in cstates.items():
            if springIndex == springLen:
                if keyIndex == keyLen:
                    score += num
                continue
            schar = springs[springIndex]
            if (schar =='#' or schar == '?') and keyIndex < keyLen and expectWorking == 0:
                if schar == '?' and cc == 0:
                    nstates[(springIndex+1,keyIndex,cc,expectWorking)] += num
                
                cc += 1
                if cc == key[keyIndex] :
                    keyIndex +=1
                    cc = 0
                    expectWorking = 1
                nstates[(springIndex+1,keyIndex,cc,expectWorking)] += num
            
            elif (schar =='.' or schar == '?') and cc == 0:
                expectWorking = 0

                nstates[(springIndex+1,keyIndex,cc,expectWorking)] += num
        cstates = nstates
        nstates = defaultdict(lambda: 0)
    return score

def getPermutations(l):
    row = l.strip().split()
    key = tuple(int(v) for v in row[1].split(',')*5)

    springs = '?'.join([row[0]]*5)

    return searchString(key, springs)

if __name__ == '__main__':
    with open('Day 12/day12.txt') as file:
        print(sum(map(getPermutations, iter(file))))