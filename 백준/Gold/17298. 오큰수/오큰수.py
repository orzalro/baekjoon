import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

stack = []
result = [-1 for _ in range(n)]

for i, num in enumerate(numbers):
    while stack:
        if stack[-1][1] < num:
            result[stack[-1][0]] = num
            stack.pop()
        else:
            break
    stack.append([i, num])

print(*result)