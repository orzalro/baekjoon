import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for middle in range(n):
    for start in range(n):
        for end in range(n):
            cost[start][end] = min(cost[start][end], cost[start][middle] + cost[middle][end])

[print(*[c if c != float('inf') else 0 for c in row]) for row in cost]