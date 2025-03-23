import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

q = deque()
q.append(n)
next_q = deque()
visited = set()
depth = 0

while n < k:
    current = q.popleft()
    visited.add(current)
    if current == k:
        break
    if current - 1 not in visited and current - 1 <= 100000:
        next_q.append(current - 1)
    if current + 1 not in visited and current + 1 <= 100000:
        next_q.append(current + 1)
    if current * 2 not in visited and current * 2 <= 100000:
        next_q.append(current * 2)
    
    if len(q) == 0:
        q = next_q
        next_q = deque()
        depth += 1

if n > k:
    print(n - k)
else:
    print(depth)