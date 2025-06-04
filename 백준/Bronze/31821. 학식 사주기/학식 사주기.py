import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

m = int(input())
total = 0
for i in range(m):
    total += a[int(input()) - 1]

print(total)