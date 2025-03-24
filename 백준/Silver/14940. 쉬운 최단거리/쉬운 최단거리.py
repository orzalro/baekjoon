import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def bfs(y, x):
    answer[y][x] = 0
    q = [[y, x]]
    next_q = []
    count = 1

    while len(q) != 0:
        for i in q:
            y, x = i
            if x + 1 < m and matrix[y][x + 1] == 1:
                answer[y][x + 1] = count
                matrix[y][x + 1] = 0
                next_q.append([y, x + 1])
            if x > 0 and matrix[y][x - 1] == 1:
                answer[y][x - 1] = count
                matrix[y][x - 1] = 0
                next_q.append([y, x - 1])
            if y + 1 < n and matrix[y + 1][x] == 1:
                answer[y + 1][x] = count
                matrix[y + 1][x] = 0
                next_q.append([y + 1, x])
            if y > 0 and matrix[y - 1][x] == 1:
                answer[y - 1][x] = count
                matrix[y - 1][x] = 0
                next_q.append([y - 1, x])

        q = next_q
        next_q = []
        count += 1

answer = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            answer[i][j] = 0
        elif matrix[i][j] == 2:
            index = [i, j]

bfs(index[0], index[1])

for i in answer:
    print(' '.join(map(str, i)))