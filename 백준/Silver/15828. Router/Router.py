import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
while True:
    data = int(input())
    if data == -1:
        break
    elif data == 0:
        q.popleft()
    elif len(q) < n:
        q.append(data)

if len(q) != 0:
    print(*q, sep = ' ')
else:
    print('empty')