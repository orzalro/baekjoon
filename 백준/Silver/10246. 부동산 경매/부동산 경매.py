import sys
input = sys.stdin.readline

l = []
while True:
    n = int(input())
    if n == 0:
        break
    l.append(n)
if not l:
    exit(0)

max_num = max(l)
values = [1 for _ in range(max_num + 1)]
if max_num >= 1:
    values[1] = 0

total = 0
for cur in range(2, max_num + 1):
    total += cur - 1
    if cur * 2 + total > max_num:
        break
    imax = (max_num - total) // cur
    for i in range(2, imax + 1):
        values[cur * i + total] += 1

result = []
for n in l:
    result.append(values[n])
print(*result, sep='\n')