import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

def calc():
    answer = 0
    visited = set()
    visited.add(1)
    h = []

    for w, v in graph[1]:
        heapq.heappush(h, [w, v])
    
    while h:
        w1, v1 = heapq.heappop(h)
        if v1 not in visited:
            answer += w1
            visited.add(v1)
            for w2, v2 in graph[v1]:
                if v2 not in visited:
                    heapq.heappush(h, [w2, v2])

    return answer

print(calc())