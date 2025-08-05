import sys
input = sys.stdin.readline

query = []
choco = []
coffee = []

while True:
    temp = input().split()
    if temp:
        if temp[0] == 'Query':
            query.append(int(temp[1]))
        elif temp[0] == 'Chocolate':
            choco.append([int(temp[1]), float(temp[2])])
        else:
            coffee.append([int(temp[1]), float(temp[2])])
    else:
        break

query.sort()
for t1 in query:
    r = 0
    for t2, n in choco:
        if t2 > t1:
            continue
        t = t1 - t2
        choco_radius = 8 * n - t / 12
        if choco_radius > 0:
            r += choco_radius
    for t2, n in coffee:
        if t2 > t1:
            continue
        t = t1 - t2
        coffee_radius = 2 * n - t * t / 79
        if coffee_radius > 0:
            r += coffee_radius
    print(t1, round(max(1.0, r) + 0.0000001, 1))