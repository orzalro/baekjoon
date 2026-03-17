import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

clean = 0

while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        clean += 1
    if any([graph[r - 1][c] == 0, graph[r][c + 1] == 0, graph[r + 1][c] == 0, graph[r][c - 1] == 0]):
        d = [0, 1, 2, 3][d - 1]
        if d == 0 and graph[r - 1][c] == 0:
            r -= 1
            continue
        if d == 1 and graph[r][c + 1] == 0:
            c += 1
            continue
        if d == 2 and graph[r + 1][c] == 0:
            r += 1
            continue
        if d == 3 and graph[r][c - 1] == 0:
            c -= 1
            continue
    else:
        if d == 0 and graph[r + 1][c] != 1:
            r += 1
            continue
        if d == 1 and graph[r][c - 1] != 1:
            c -= 1
            continue
        if d == 2 and graph[r - 1][c] != 1:
            r -= 1
            continue
        if d == 3 and graph[r][c + 1] != 1:
            c += 1
            continue
        break

print(clean)