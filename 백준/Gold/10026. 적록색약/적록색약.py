import sys

input = sys.stdin.readline

n = int(input())
l = [[] for _ in range(n)]

for i in range(n):
    for char in input().strip():
        l[i].append(char)

def bfs(i, j, check):
    q = [[i, j]]
    next_q = []
    color = l[i][j]
    l[i][j] = check

    while len(q) != 0:
        for i in q:
            y, x = i
            if x + 1 < len(l[y]) and l[y][x + 1] == color:
                l[y][x + 1] = check
                next_q.append([y, x + 1])
            if x > 0 and l[y][x - 1] == color:
                l[y][x - 1] = check
                next_q.append([y, x - 1])
            if y + 1 < n and l[y + 1][x] == color:
                l[y + 1][x] = check
                next_q.append([y + 1, x])
            if y > 0 and l[y - 1][x] == color:
                l[y - 1][x] = check
                next_q.append([y - 1, x])
        q = next_q
        next_q = []

count = 0

for i in range(n):
    for j in range(len(l[i])):
        if l[i][j] in ['R', 'G', 'B']:
            check = 'C' if l[i][j] == 'B' else 'RG'
            bfs(i, j, check)
            count += 1

rg_count = 0
for i in range(n):
    for j in range(len(l[i])):
        if l[i][j] in ['RG', 'C']:
            check = 'G' if l[i][j] == 'RG' else 'B'
            bfs(i, j, check)
            rg_count += 1

print(count, rg_count)