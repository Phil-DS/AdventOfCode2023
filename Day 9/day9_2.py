with open('Day 9/day9.txt') as file:
    score = 0

    for line in file:
        values = [int(v) for v in line.strip().split()]
        # print(values)
        sequences = []
        current = [*values]
        sequences.append(current)
        while not all((l == 0 for l in current)):
            current = [b-a for a,b in zip(current,current[1:])]
            sequences.append(current)

        nextVal = 0
        for s in reversed(sequences):
            nextVal = s[0] - nextVal

        score += nextVal

    print(score)