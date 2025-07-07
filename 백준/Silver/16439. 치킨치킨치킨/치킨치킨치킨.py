import sys
input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())

l = []
for i in range(n):
    l.append(list(map(int, input().split())))

max_total = 0
for c in combinations(range(m), 3):
    total = 0
    for i in l:
        total += max(map(lambda x: i[x], c))
    max_total = max(max_total, total)
print(max_total)