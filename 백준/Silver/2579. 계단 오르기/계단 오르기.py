import sys


n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline().strip()))

d = [0] * n

if n <= 2:
    print(sum(l))
else:
    d[0] = l[0]
    d[1] = l[0] + l[1]
    for i in range(2, n):
        d[i] = max(d[i - 3] + l[i - 1] + l[i], d[i - 2] + l[i])
    print(d[n-1])