import sys
from itertools import accumulate

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[0] * n]
for _ in range(n):
    matrix.append([a + b for a, b in zip(matrix[-1], list(accumulate(map(int, input().split()))))])
del matrix[0]

for _ in range(m):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    minus = 0
    if x1 > 0: minus += matrix[x1 - 1][y2]
    if y1 > 0: minus += matrix[x2][y1 - 1]
    if x1 > 0 and y1 > 0: minus -= matrix[x1 - 1][y1 - 1]
    print(matrix[x2][y2] - minus)