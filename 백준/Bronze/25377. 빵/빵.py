import sys
input = sys.stdin.readline

n = int(input())

m = 1001
for i in range(n):
    a, b = map(int, input().split())
    if a <= b:
        m = min(m, b)

print(m if m != 1001 else -1)