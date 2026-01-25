import sys
input = sys.stdin.readline

from itertools import product
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

for p in product(l, repeat=m):
    print(*p)