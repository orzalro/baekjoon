import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
[print(*c) for c in combinations(sorted(nums), m)]