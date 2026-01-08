import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    for word in input().split():
        print(word[::-1], end=' ')
    print()