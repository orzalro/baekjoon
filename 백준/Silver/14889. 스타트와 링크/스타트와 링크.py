import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

min_gap = float('inf')

def calc(c):
    if len(c) == 2:
        i, j = c
        return matrix[i][j] + matrix[j][i]
    else:
        result = 0
        for c_divide in combinations(c, 2):
            result += calc(c_divide)
        return result

for c in combinations(range(n), n // 2):
    c_set = set(c)

    team1 = calc(list(c))
    team2 = calc([x for x in range(n) if x not in c_set])
    min_gap = min(min_gap, abs(team1 - team2))

print(min_gap)