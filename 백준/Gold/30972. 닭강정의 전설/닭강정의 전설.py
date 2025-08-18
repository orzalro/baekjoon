import sys
input = sys.stdin.readline

n = int(input())
k = [[*map(int, input().split())] for _ in range(n)]
q = int(input())

for i in range(n):
    for j in range(n):
        if j > 0:
            k[i][j] += k[i][j - 1]
        if i > 0:
            k[i][j] += k[i - 1][j]
        if j > 0 and i > 0:
            k[i][j] -= k[i - 1][j - 1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = (r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    result = -k[r2][c2]
    if r1 > 0:
        result += k[r1 -1][c2]
    if c1 > 0:
        result += k[r2][c1 - 1]
    if r1 > 0 and c1 > 0:
        result -= k[r1 - 1][c1 - 1]

    if r1 + 1 < r2 and c1 + 1 < c2:
        result += (k[r2 - 1][c2 - 1] - k[r2 - 1][c1] - k[r1][c2 - 1] + k[r1][c1]) * 2
    print(result)