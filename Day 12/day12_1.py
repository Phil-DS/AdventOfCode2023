def permutateString(s: str):
    poses = [i for i,c in enumerate(s) if c == '?']

    if not poses:
        yield s
        return

    o = [*s]
    for i in range(1<<len(poses)):
        for j,pos in enumerate(poses):
            o[pos] = '#' if (1 << j) & i else '.'
        yield ''.join(o)
        
def getPermutations(l):
    row = l.strip().split()
    key = tuple(int(v) for v in row[1].split(','))
    count = 0
    for layout in permutateString(row[0]):
        currentKey = tuple(len(s) for s in layout.split('.') if s)
        if key == currentKey:
            count += 1
    
    print(count)
    return count

if __name__ == '__main__':
    with open('Day 12/day12.txt') as file:
        print(sum(map(getPermutations, iter(file))))