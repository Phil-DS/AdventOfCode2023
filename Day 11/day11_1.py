

import math


with open('Day 11/day11.txt') as file:
    field = [l.strip() for l in file]

    emptyMask = [False for _ in field[0]]
    for l in field:
        for i,c in enumerate(l):
            emptyMask[i] = emptyMask[i] or c == '#'
    
    print(emptyMask)

    field = [''.join((c if emptyMask[i] else '..' for i,c in enumerate(l))) for l in field]

    print(field)

    emptyField = '.'*len(field[0])

    emptyMask = reversed([None if any(c == '#' for c in l) else i for i,l in enumerate(field)])

    for i in emptyMask:
        if i is None:
            continue
        field.insert(i,emptyField)

    print(*field, sep='\n')
    poses = [(i,j) for i in range(len(field[0])) for j in range(len(field)) if field[j][i] == '#']

    print(poses)

    finalScore = 0
    for i in range(len(poses)-1):
        for j in range(i+1,len(poses)):
            finalScore+= abs(poses[i][0]-poses[j][0])+abs(poses[i][1]-poses[j][1])
    print(finalScore)
