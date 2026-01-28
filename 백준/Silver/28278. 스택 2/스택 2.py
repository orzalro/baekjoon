import sys
input = sys.stdin.readline

n = int(input())
c_l = [input().split() for _ in range(n)]
stack = []

for c in c_l:
    if c[0] == '1':
        stack.append(c[1])
    elif c[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif c[0] == '3':
        print(len(stack))
    elif c[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)