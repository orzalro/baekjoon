import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():
    visited = set()
    visited.add(a)
    q = [a]
    new_q = []
    count = 1

    while q:
        for i in q:
            for j in graph[i]:
                if j == b:
                    return count
                if j not in visited:
                    visited.add(j)
                    new_q.append(j)
        q = new_q
        new_q = []
        count += 1
    return -1

print(bfs())