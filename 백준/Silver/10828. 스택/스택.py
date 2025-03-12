import sys

n = int(sys.stdin.readline().strip())
stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop() if len(stack) >= 1 else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif command[0] == 'top':
        print(stack[-1] if len(stack) >= 1 else -1)