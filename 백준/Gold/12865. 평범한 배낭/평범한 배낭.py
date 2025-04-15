import sys

input = sys.stdin.readline

n, k = map(int, input().split())

p = []
for i in range(n):
    w, v = map(int, input().split())
    p.append([w, v])

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, k + 1):
        if p[i - 1][0] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - p[i - 1][0]] + p[i - 1][1])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[-1][-1])