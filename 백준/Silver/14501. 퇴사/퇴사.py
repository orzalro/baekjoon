import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n)]
for i in range(n):
    t, p = map(int, input().split())
    if i + t - 1 < n:
        dp[i] = max(dp[i], dp[i - 1])
        dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)
    else:
        dp[i] = max(dp[i], dp[i - 1])

print(max(dp))