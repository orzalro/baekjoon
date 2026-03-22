import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    price = int(input())
    if price <= k:
        coins.append(price)

dp = [0 for _ in range(k + 1)]
for coin in coins:
    dp[coin] += 1
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])