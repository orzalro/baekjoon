import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    string = input().strip()
    for j in range(m):
        maze[i][j] = int(string[j])

def bfs():
    visited = [item[:] for item in maze]
    y, x, count = 0, 0, 1
    q = []
    while True:
        if x == m - 1 and y == n - 1:
            break
        visited[y][x] = 0
        if x + 1 < m and visited[y][x + 1] == 1:
            visited[y][x + 1] = 0
            q.append([y, x + 1, count + 1])
        if y + 1 < n and visited[y + 1][x] == 1:
            visited[y + 1][x] = 0
            q.append([y + 1, x, count + 1])
        if x - 1 >= 0 and visited[y][x - 1] == 1:
            visited[y][x - 1] = 0
            q.append([y, x - 1, count + 1])
        if y - 1 >= 0 and visited[y - 1][x] == 1:
            visited[y - 1][x] = 0
            q.append([y - 1, x, count + 1])
        y, x, count = map(int, q.pop(0))
    print(count)

bfs()