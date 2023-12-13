

import math

expansionAmount = 1000000 - 1

with open('Day 11/day11.txt') as file:
    field = [l.strip() for l in file]

    emptyMaskX = [False for _ in field[0]]
    for l in field:
        for i,c in enumerate(l):
            emptyMaskX[i] = emptyMaskX[i] or c == '#'

    emptyMaskY = [any(c == '#' for c in l) for l in field]

    poses = []
    xExpansion = 0
    for i in range(len(field[0])):
        if not emptyMaskX[i]:
            xExpansion += expansionAmount
            continue
        yExpansion = 0
        for j in range(len(field)):
            if not emptyMaskY[j]:
                yExpansion += expansionAmount
                continue
            if field[j][i] == '#':
                poses.append((i+xExpansion,j+yExpansion))

    print(poses)

    finalScore = 0
    for i in range(len(poses)-1):
        for j in range(i+1,len(poses)):
            finalScore+= abs(poses[i][0]-poses[j][0])+abs(poses[i][1]-poses[j][1])
    print(finalScore)
#[(0, 2), (0, 11), (1, 6), (4, 0), (5, 11), (8, 5), (9, 1), (9, 10), (12, 7)]