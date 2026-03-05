import sys
input = sys.stdin.readline

n = int(input())

dp = [[] for _ in range(n)]
dp[0] = [0] + [1 for _ in range(1, 10)]

for i in range(1, n):
    for num in range(10):
        if num == 0:
            dp[i].append(dp[i-1][num+1])
        elif num == 9:
            dp[i].append(dp[i-1][num-1])
        else:
            dp[i].append(dp[i-1][num-1] + dp[i-1][num+1])

print(sum(dp[n - 1]) % 1000000000)