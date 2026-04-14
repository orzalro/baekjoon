import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
t = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    t[a - 1].append((c, b - 1))

def calc(a, b):
    d = [float('inf')] * n
    d[a] = 0
    visited = set()

    h = [(0, a)]
    while h:
        _, u = heapq.heappop(h)
        if u in visited:
            continue
        visited.add(u)
        for c, v in t[u]:
            if d[v] > d[u] + c:
                d[v] = d[u] + c
                heapq.heappush(h, (d[v], v))
    
    return d[b]

result = [calc(i, x - 1) + calc(x - 1, i) for i in range(n)]
print(max(result))