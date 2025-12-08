import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    visited = []
    temp = 1
    for _ in range(b):
        temp *= a
        num = temp % 10
        if num in visited:
            break
        else:
            visited.append(num)
    num = visited[(b - 1) % len(visited)]
    print(num if num != 0 else 10)