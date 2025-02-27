import sys

n, m = map(int, (sys.stdin.readline().split()))
l = list(map(int, (sys.stdin.readline().split())))
l.sort()

left = 0
middle = 1
right = 2
max = 0

while True:
    s = l[left] + l[middle] + l[right]
    if s < m:
        right += 1
        if s > max:
            max = s
    elif s > m:
        middle = middle + 1
        right = middle + 1
    else:
        max = s
        break
    if right >= len(l):
        middle = middle + 1
        right = middle + 1
    if middle >= len(l) - 1:
        left = left + 1
        middle = left + 1
        right = middle + 1
    if left >= len(l) - 2:
        break

print(max)