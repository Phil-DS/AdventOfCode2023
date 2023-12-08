
with open('Day 6/day6.txt') as file:
    times = list(map(int,file.readline().split()[1:]))
    distances = list(map(int,file.readline().split()[1:]))
    
    score = 1
    for t,d in zip(times,distances):
        count = 0
        for th in range(t):
            if (th * (t-th)) > d:
                count += 1
        if count:
            score *= count
    print(score)