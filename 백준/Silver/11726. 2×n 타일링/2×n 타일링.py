import sys

input = sys.stdin.readline

n = int(input().strip())

d = [0, 1, 2]
for i in range(3, 1001):
    d.append(sum(d[i - 2:i]))

print(d[n] % 10007)