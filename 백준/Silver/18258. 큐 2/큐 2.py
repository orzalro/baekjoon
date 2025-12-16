import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    i = input().split()
    if i[0] == 'push':
        q.append(int(i[1]))
    elif i[0] == 'pop':
        try: print(q.popleft())
        except: print(-1)
    elif i[0] == 'size':
        print(len(q))
    elif i[0] == 'empty':
        print(0 if len(q) else 1)
    elif i[0] == 'front':
        try: print(q[0])
        except: print(-1)
    elif i[0] == 'back':
        try: print(q[-1])
        except: print(-1)