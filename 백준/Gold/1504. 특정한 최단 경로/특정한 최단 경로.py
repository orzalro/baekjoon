import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1].append([c, b - 1])
    graph[b - 1].append([c, a - 1])
v1, v2 = map(int, input().split())

def calc(u, v):
    d = [float('inf')] * n
    d[u] = 0
    visited = set()
    h = [(0, u)]

    while h:
        _, a = heapq.heappop(h)
        if a in visited:
            continue
        visited.add(a)
        for c, b in graph[a]:
            if d[a] + c < d[b]:
                d[b] = d[a] + c
                heapq.heappush(h, (d[b], b))

    return d[v]

answer1 = calc(0, v1 - 1) + calc(v1 - 1, v2 - 1) + calc(v2 - 1, n - 1)
answer2 = calc(0, v2 - 1) + calc(v2 - 1, v1 - 1) + calc(v1 - 1, n - 1)
answer = min(answer1, answer2)
print(answer if answer != float('inf') else -1)