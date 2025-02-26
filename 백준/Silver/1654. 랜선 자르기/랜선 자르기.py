import sys

k, n = map(int, sys.stdin.readline().split())

l = []
t = 0
for i in range(k):
    a = int(sys.stdin.readline().strip())
    t += a
    l.append(a)

ma = t
mi = 0
d = 1

while True:
    count = 0
    pre = d
    for i in l:
        count += i // d
    if count >= n:
        mi = d
        d = int((d + ma) / 2)
    elif count < n:
        ma = d
        d = int((d + mi) / 2)
    if d == pre:
        break

print(d)