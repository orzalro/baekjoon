import sys
import heapq

input = sys.stdin.readline

def calc(n, route, start, end):
    heap = [[0, start]]
    s = set()
    d = [float('inf')] * n
    d[start] = 0
    while heap:
        _, cur = heapq.heappop(heap)
        if cur in s: continue
        s.add(cur)
        for dest, dist in route[cur]:
            if d[cur] + dist < d[dest]:
                d[dest] = d[cur] + dist
                heapq.heappush(heap, [d[dest], dest])
    
    return d[end]


n = int(input())
m = int(input())

routes = [[] for _ in range(n)]
for _ in range(m):
    start, dest, dist = map(int, input().split())
    routes[start - 1].append([dest - 1, dist])

start, dest = map(int, input().split())
print(calc(n, routes, start - 1, dest - 1))