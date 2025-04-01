import sys

input = sys.stdin.readline

n, m = map(int, (input().split()))
l = []

for i in range(n):
    l.append(list(map(int, input().split())))

def calc(x, y):
    max_num = 0
    # I
    if x + 3 < m:
        max_num = max(max_num, sum([l[y][i] for i in range(x, x + 4)]))
    if y + 3 < n:
        max_num = max(max_num, sum([l[i][x] for i in range(y, y + 4)]))

    # L
    if x + 2 < m and y + 1 < n:
        max_num = max(max_num, sum([l[y][i] for i in range(x, x + 3)]) + l[y + 1][x + 2], sum([l[y][i] for i in range(x, x + 3)]) + l[y + 1][x], sum([l[y + 1][i] for i in range(x, x + 3)]) + l[y][x])
    if x + 1 < m and y + 2 < n:
        max_num = max(max_num, sum([l[i][x] for i in range(y, y + 3)]) + l[y][x + 1], sum([l[i][x] for i in range(y, y + 3)]) + l[y + 2][x + 1], sum([l[i][x + 1] for i in range(y, y + 3)]) + l[y][x])
    if x + 2 < m and y > 0:
        max_num = max(max_num, sum([l[y][i] for i in range(x, x + 3)]) + l[y - 1][x + 2])
    if x > 0 and y + 2 < n:
        max_num = max(max_num, sum([l[i][x] for i in range(y, y + 3)]) + l[y + 2][x - 1])

    # S
    if x + 1 < m and y + 2 < n:
        max_num = max(max_num, sum([l[i][x] for i in range(y, y + 2)]) + sum([l[i + 1][x + 1] for i in range(y, y + 2)]))
    if x > 0 and y + 2 < n:
        max_num = max(max_num, sum([l[i][x] for i in range(y, y + 2)]) + sum([l[i + 1][x - 1] for i in range(y, y + 2)]))
    if y + 1 < n and x + 2 < m:
        max_num = max(max_num, sum([l[y][i] for i in range(x, x + 2)]) + sum([l[y + 1][i + 1] for i in range(x, x + 2)]))
    if y > 0 and x + 2 < m:
        max_num = max(max_num, sum([l[y][i] for i in range(x, x + 2)]) + sum([l[y - 1][i + 1] for i in range(x, x + 2)]))
    
    # T
    if x + 2 < m and y + 1 < n:
        max_num = max(max_num, sum([l[y][i] for i in range(x, x + 3)]) + l[y + 1][x + 1])
    if x + 1 < m and y + 2 < n:
        max_num = max(max_num, sum([l[i][x] for i in range(y, y + 3)]) + l[y + 1][x + 1])
    if 1 < x + 1 < m and y + 1 < n:
        max_num = max(max_num, sum([l[y + 1][i] for i in range(x - 1, x + 2)]) + l[y][x])
    if x + 1 < m and 1 < y + 1 < n:
        max_num = max(max_num, sum([l[i][x + 1] for i in range(y - 1, y + 2)]) + l[y][x])

    # O
    if x + 1 < m and y + 1 < n:
        max_num = max(max_num, sum([l[y][i] for i in range(x, x + 2)]) + sum([l[y + 1][i] for i in range(x, x + 2)]))

    return max_num

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, calc(j, i))
print(answer)