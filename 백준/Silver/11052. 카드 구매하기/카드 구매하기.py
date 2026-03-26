import sys
input = sys.stdin.readline

n = int(input())
dp = [0]
dp.extend(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i - j - 1] + dp[j + 1])

print(dp[-1])