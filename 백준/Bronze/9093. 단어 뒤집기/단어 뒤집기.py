import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    [print(word[::-1], end=' ') for word in input().split()]
    print()