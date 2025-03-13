import sys


n, k = map(int, (sys.stdin.readline().split()))
l = []
count = 0

for i in range(n):
    l.append(int(sys.stdin.readline().strip()))

for i in range(len(l), 0, -1):
    if l[i - 1] <= k:
        m = k // l[i - 1]
        k -= m * l[i - 1]
        count += m

print(count)