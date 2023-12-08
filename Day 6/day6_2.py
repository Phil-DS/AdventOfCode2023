
with open('Day 6/day6.txt') as file:
    t = int(''.join(file.readline().split()[1:]))
    d = int(''.join(file.readline().split()[1:]))

    lh, rh = 0,0
    for th in range(t):
        if (th * (t-th)) > d:
            lh = th
            break
    for th in range(t,0,-1):
        if (th * (t-th)) > d:
            rh = th
            break
    print(lh,rh)
    print(rh - lh + 1)