import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
def fill(x1, y1, x2, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1
for _ in range(k):
    fill(*map(int, input().split()))

def bfs(x, y):
    q = [[x, y]]
    new_q = []
    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        for x, y in q:
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    new_q.append([nx, ny])
        q = new_q
        new_q = []
    
    return count

answer = []
for y in range(m):
    for x in range(n):
        if graph[y][x] == 0:
            graph[y][x] = 1
            answer.append(bfs(x, y))

print(len(answer))
print(*sorted(answer))