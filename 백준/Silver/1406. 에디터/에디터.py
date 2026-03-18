import sys
from collections import deque
input = sys.stdin.readline

left = deque(input().strip())
right = deque()
m = int(input())

for _ in range(m):
    command = input().split()
    if command[0] == 'L' and left:
        right.appendleft(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.popleft())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(*left, *right, sep='')