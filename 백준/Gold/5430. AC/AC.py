import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

def ac(p, x):
    reverse = 0
    while len(p) != 0:
        command = p[0]
        p = p[1:]
        if command == 'R':
            reverse = 1 if reverse == 0 else 0
        elif command == 'D':
            if len(x) > 0:
                if reverse == 0:
                    x.popleft()
                else:
                    x.pop()
            else:
                return 'error'
    if reverse == 1:
        x.reverse()
    return '[' + ','.join(map(str, x)) + ']'

for i in range(t):
    p = input().strip()
    n = int(input())
    x = input()
    x = deque(map(int, x.strip()[1:-1].split(','))) if n > 0 else []

    print(ac(p, x))