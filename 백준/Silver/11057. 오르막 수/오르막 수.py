import sys
input = sys.stdin.readline

n = int(input())
dp = [[1] + [0] * (n - 1) for _ in range(10)]

for i in range(1, n):
    for j in range(10):
        for k in range(j, 10):
            dp[k][i] += dp[j][i - 1]

print(sum([num[-1] for num in dp]) % 10007)