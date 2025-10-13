import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

n = c - b
if n > 0: print(a // n + 1)
else: print(-1)