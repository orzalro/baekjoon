import sys

n = int(sys.stdin.readline().strip())

list = []
for i in range(n):
    x, y = map(int, (sys.stdin.readline().split()))
    list.append((x, y))

rank_list = []
for i in list:
    rank = 1
    for j in list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    rank_list.append(rank)

print(' '.join(map(str, rank_list)))