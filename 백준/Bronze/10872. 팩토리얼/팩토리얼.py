import sys
from functools import reduce
input = sys.stdin.readline

n = int(input())
if n:
    print(reduce(lambda x, y: x * y, range(1, n + 1)))
else:
    print(1)