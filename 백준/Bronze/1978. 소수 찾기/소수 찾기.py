import sys

n = int(sys.stdin.readline().strip())
s = list(map(int, (sys.stdin.readline().split())))

p = [2]
for i in range(3, 1001):
    c = 1
    for j in p:
        if i % j == 0:
            c = 0
            break
    if c == 1: p.append(i)

count = 0
for i in s:
    if i in p: count += 1
print(count)