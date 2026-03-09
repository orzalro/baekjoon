import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    q = [[x, y]]
    next_q = []

    while q:
        for x, y in q:
            if x + 1 < m and graph[y][x + 1] == 0:
                graph[y][x + 1] = 3
                next_q.append([x + 1, y])
            if x > 0 and graph[y][x - 1] == 0:
                graph[y][x - 1] = 3
                next_q.append([x - 1, y])
            if y + 1 < n and graph[y + 1][x] == 0:
                graph[y + 1][x] = 3
                next_q.append([x, y + 1])
            if y > 0 and graph[y - 1][x] == 0:
                graph[y - 1][x] = 3
                next_q.append([x, y - 1])
        q = next_q
        next_q = []

def calc(i):
    if i == 0:
        # 전염
        for y in range(n):
            for x in range(m):
                if graph[y][x] == 2:
                    bfs(x, y)

        # 안전구역 카운트
        count = 0
        for y in range(n):
            for x in range(m):
                if graph[y][x] == 0:
                    count += 1

        global max_count
        max_count = max(max_count, count)

        # 복구
        for y in range(n):
            for x in range(m):
                if graph[y][x] == 3:
                    graph[y][x] = 0
    else:
        for y in range(n):
            for x in range(m):
                if graph[y][x] == 0:
                    graph[y][x] = 1
                    calc(i - 1)
                    graph[y][x] = 0

max_count = 0
calc(3)
print(max_count)