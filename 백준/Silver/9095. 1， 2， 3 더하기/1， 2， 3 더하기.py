import sys


n = int(sys.stdin.readline().strip())

d = [0] * 11

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = sum(d[i-3:i])

for i in range(n):
    print(d[int(sys.stdin.readline().strip())])