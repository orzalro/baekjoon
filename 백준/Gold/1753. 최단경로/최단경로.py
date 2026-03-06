import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
l = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    l[u].append([v, w])

d = [float('inf') if i != k else 0 for i in range(V + 1)]
visited = set()
heap = [[0, k]]

while heap:
    _, cur = heapq.heappop(heap)
    if cur in visited: continue
    visited.add(cur)

    for v, w in l[cur]:
        if d[cur] + w < d[v]:
            d[v] = d[cur] + w
            heapq.heappush(heap, [d[v], v])

for w in d[1:]:
    if w == float('inf'):
        print('INF')
    else:
        print(w)