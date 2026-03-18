import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
m = int(input())

for _ in range(m):
    command = input().split()
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

right.reverse()
left.extend(right)
print(''.join(left))