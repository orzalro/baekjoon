import sys

input = sys.stdin.readline

n, d, k = map(int, input().split())
s = max(list(map(int, input().split())))
count = d // (k // s) if d % (k // s) != 0 else d // (k // s) - 1
print(count)