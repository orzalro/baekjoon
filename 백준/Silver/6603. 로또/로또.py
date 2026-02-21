import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    nums = input().split()
    if nums[0] == '0':
        break
    [print(*c) for c in combinations(nums[1:], 6)]
    print()