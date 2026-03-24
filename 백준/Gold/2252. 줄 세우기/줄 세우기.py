import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

smaller = [[] for _ in range(n)]
taller = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    smaller[a].append(b)
    taller[b] += 1

q = deque(i for i in range(n) if taller[i] == 0)
result = []

while q:
    i = q.popleft()
    result.append(i + 1)
    for j in smaller[i]:
        taller[j] -= 1
        if taller[j] == 0:
            q.append(j)

print(' '.join(map(str, result)))