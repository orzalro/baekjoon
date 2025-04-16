import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

chicken = []
house = []
for i in range(n):
    for j, num in enumerate(map(int, input().split())):
        if num == 1: house.append([i, j])
        elif num == 2: chicken.append([i, j])

def calc(house, chicken, m):
    distance_from_house = [[99 for _ in range(len(chicken))] for _ in range(len(house))]
    distance_from_chicken = [[99 for _ in range(len(house))] for _ in range(len(chicken))]

    for i, h_coord in enumerate(house):
        h_x, h_y = h_coord
        for j, c_coord in enumerate(chicken):
            c_x, c_y = c_coord
            temp = ((h_x - c_x) if h_x > c_x else (c_x - h_x)) + ((h_y - c_y) if h_y > c_y else (c_y - h_y))
            distance_from_house[i][j] = temp
            distance_from_chicken[j][i] = temp

    if m == 1: return min(sum(c) for c in distance_from_chicken)
    elif m == len(chicken): return sum(min(c) for c in distance_from_house)
    else:
        min_total = float('inf')
        for combine in combinations(range(len(chicken)), m):
            total = 0
            for d in distance_from_house:
                total += min(d[i] for i in combine)
            min_total = min(min_total, total)
        return min_total

print(calc(house, chicken, m))