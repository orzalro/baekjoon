import sys
input = sys.stdin.readline

n, m = map(int, input().split())
print(*range(m * 2, m * (n + 1) + 1, m), sep=' ')