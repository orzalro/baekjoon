import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

if n < b:
    print(n)
else:
    n = n - b
    print(min(n, a // 2) + b)