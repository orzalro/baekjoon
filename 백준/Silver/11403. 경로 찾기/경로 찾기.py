import sys

input = sys.stdin.readline

n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def dfs(y, v):
    v.append(y)
    for i in range(n):
        if matrix[y][i] == 1 and i not in v:
            dfs(i, v)

visited = [[] for _ in range(n)]

for i in range(n):
    v = []
    for j in range(n):
        if matrix[i][j] == 1:
            dfs(j, v)
    visited[i] = v

for i in range(n):
    for j in visited[i]:
        matrix[i][j] = 1

for i in matrix:
    print(' '.join(map(str, i)))