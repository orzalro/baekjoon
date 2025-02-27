import sys

n = int(sys.stdin.readline().strip())

if n < 55:
    c = 0
else:
    c = n - 55

for i in range(c, n):
    t = i
    for j in str(i):
        t = t + int(j)
    if t == n:
        o = i
        break
    o = 0
print(o)