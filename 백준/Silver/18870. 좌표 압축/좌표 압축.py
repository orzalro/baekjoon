import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))
d = {}

for i, key in enumerate(sorted(set(l))):
    if key not in d: d[key] = i

for i in l:
	print(d[i])     