import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[0 for _ in range(m + 1)]]
for _ in range(n):
    l.append([0 ,*map(int, input().split())])

for i in range(1, n + 1):
    for j in range(1, m + 1):
        l[i][j] += l[i - 1][j] + l[i][j - 1] - l[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(l[x][y] - l[x][j - 1] - l[i - 1][y] + l[i - 1][j - 1])