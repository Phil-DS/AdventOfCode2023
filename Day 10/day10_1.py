deltas = {
    '|': {
        (0, 1): (0, 1),
        (0,-1): (0,-1)
    }, # is a vertical pipe connecting north and south.
    '-': {
        ( 1,0): ( 1,0),
        (-1,0): (-1,0)
    }, # is a horizontal pipe connecting east and west.
    'L': {
        (0,1): (1,0),
        (-1,0): (0,-1)
    }, # is a 90-degree bend connecting north and east.
    'J': {
        (0,1): (-1,0),
        (1,0): (0,-1)
    }, # is a 90-degree bend connecting north and west.
    '7': {
        (0,-1): (-1,0),
        (1,0): (0,1)
    }, # is a 90-degree bend connecting south and west.
    'F': {
        (0,-1): (1,0),
        (-1,0): (0,1)
    }, # is a 90-degree bend connecting south and east.
}

def getStart(file):
    for i,line in enumerate(file):
        for j,c in enumerate(line):

            if c == 'S':
                return (j,i)
            
def routeGen(area,start,initialDirection):
    direction = initialDirection
    currentPos = (start[0]+direction[0],start[1]+direction[1])
    while currentPos != start:

        if area[currentPos[1]][currentPos[0]] == '.':
            yield None
            break

        if currentPos[0] < 0 or currentPos[1] < 0:
            yield None
            break

        try:
            yield (currentPos,direction)
            symbol = area[currentPos[1]][currentPos[0]]
            direction = deltas[symbol][direction]
            currentPos = (currentPos[0]+direction[0],currentPos[1]+direction[1])
        except Exception as e:
            print(e)
            yield None
            break


with open('Day 10/day10.txt') as file:
    start = getStart(file)
    file.seek(0)
    area = [l.strip() for l in file.readlines()]
    print(start)
    print(area)
    

    routeA = []
    routeB = []

    directions = {
        (1,0): [],
        (0,1): [],
        (-1,0): [],
        (0,-1): [],
        }
    maxLen = 0
    dirsToCheck = directions.keys()
    for k in dirsToCheck:
        if len(directions[k]):
            continue
        
        for p in routeGen(area,start,k):
            if p is None:
                break
            directions[k].append(p)
        if p is None:
            continue
        directions[(p[1][0]*-1,p[1][1]*-1)] = directions[k]
        maxLen = max(((len(directions[k])+1)//2,maxLen))
    print(maxLen)
    
