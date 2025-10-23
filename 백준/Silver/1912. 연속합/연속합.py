import sys
input = sys.stdin.readline

n = int(input())
l = [*map(int, input().split())]
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = max(0, dp[i - 1]) + l[i - 1]

print(max(dp[1:]))