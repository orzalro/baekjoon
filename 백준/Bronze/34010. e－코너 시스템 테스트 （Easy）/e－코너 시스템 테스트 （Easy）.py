import sys
input = sys.stdin.readline

n = int(input())

for i in range(2 * n - 1):
    _ = input()

print((n - 1) * 2, 2 * (n - 1) - 1)