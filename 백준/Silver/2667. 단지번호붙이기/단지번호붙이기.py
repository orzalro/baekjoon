import sys

input = sys.stdin.readline

n = int(input())

l = [[0] * n for _ in range(n)]

for i in range(n):
    string = input().strip()
    for j in range(n):
        l[i][j] = int(string[j])

def bfs(y, x):
    l[y][x] = 0
    q = []
    q.append([y, x])
    count = 0

    while len(q) != 0:
        next_q = []
        for i in q:
            y, x = i
            if y + 1 < n and l[y + 1][x] == 1:
                l[y + 1][x] = 0
                next_q.append([y + 1, x])
            if x + 1 < n and l[y][x + 1] == 1:
                l[y][x + 1] = 0
                next_q.append([y, x + 1])
            if y - 1 >= 0 and l[y - 1][x] == 1:
                l[y - 1][x] = 0
                next_q.append([y - 1, x])
            if x - 1 >= 0 and l[y][x - 1] == 1:
                l[y][x - 1] = 0
                next_q.append([y, x - 1])
            count += 1
        q = next_q
    return count

answer = []

for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))
for i in answer:
    print(i)