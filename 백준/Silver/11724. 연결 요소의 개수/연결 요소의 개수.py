import sys
from collections import deque

input = sys.stdin.readline

def calc():
    counter = 0
    s = set() # 방문한 노드 저장용
    q = deque()

    for start in range(n): # BFS 실행
        if start not in s:
            q.append(start)
            s.add(start)
            counter += 1

            while q:
                i = q.popleft()
                for j in range(n):
                    if l[i][j] == 1 and j not in s:
                        s.add(j)
                        q.append(j)

    return counter

n, m = map(int, input().split())
l= [[0] * n for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    l[u - 1][v - 1] = 1
    l[v - 1][u - 1] = 1

print(calc())