import sys


n = int(sys.stdin.readline().strip())

d = {}
d[1] = 0

for i in range(1, n):
    if i * 3 not in d: d[i * 3] = d[i] + 1 
    elif d[i] + 1 < d[i * 3]: d[i * 3] = d[i] + 1
    if i * 2 not in d: d[i * 2] = d[i] + 1 
    elif d[i] + 1 < d[i * 2]: d[i * 2] = d[i] + 1
    if i + 1 not in d: d[i + 1] = d[i] + 1 
    elif d[i] + 1 < d[i + 1]: d[i + 1] = d[i] + 1

print(d[n])