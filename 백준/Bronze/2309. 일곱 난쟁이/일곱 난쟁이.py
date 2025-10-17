import sys
from itertools import combinations
input = sys.stdin.readline

height_list = [int(input()) for _ in range(9)]
for com in combinations(height_list, 7):
    if sum(com) == 100:
        print(*sorted(com), sep = '\n')
        exit()