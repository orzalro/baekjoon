import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
d = {}

for i in range(n):
    for item in list(map(int, input().split())):
        if item in d: d[item] += 1
        else: d[item] = 1


def task1(key, h, block, count):
    diff = key - h
    block += diff * d[key]
    count += 2 * diff * d[key]
    return block, count


def task2(key, h, block, count):
    diff = h - key
    block -= diff * d[key]
    count += diff * d[key]
    return block, count


max_h = 0
min_h = 256
for i in range(n):
    if max(d) > max_h: max_h = max(d)
    if min(d) < min_h: min_h = min(d)

land_maxh = 256
max_time = 1000000000

for h in range(min_h, max_h + 1):
    count = 0
    block = b
    for key in d:
        if key < h:
            block, count = task2(key, h, block, count)
        elif key > h:
            block, count = task1(key, h, block, count)
    if block < 0:
        continue
    if max_time > count:
        max_time = count
        land_maxh = h
    elif max_time == count and land_maxh < h:
        land_maxh = h

print(max_time, land_maxh)