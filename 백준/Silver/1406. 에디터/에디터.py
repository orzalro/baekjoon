import sys
from collections import deque
input = sys.stdin.readline

left = deque(input().strip())
right = deque()
m = int(input())

length = len(left)

cur = length
for _ in range(m):
    command = input().split()
    if command[0] == 'L' and cur > 0:
        right.appendleft(left.pop())
        cur -= 1
    elif command[0] == 'D' and cur < length:
        left.append(right.popleft())
        cur += 1
    elif command[0] == 'B' and cur > 0:
        left.pop()
        cur -= 1
        length -= 1
    elif command[0] == 'P':
        left.append(command[1])
        cur += 1
        length += 1

print(*left, *right, sep='')