import sys
input = sys.stdin.readline

n = int(input())

square = [i ** 2 for i in range(1, int(pow(n, 0.5)) + 1)]

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i in square:
        dp[i] = 1
    else:
        dp[i] = min([dp[floor] + dp[i - floor] for floor in square if floor < i])

print(dp[n])