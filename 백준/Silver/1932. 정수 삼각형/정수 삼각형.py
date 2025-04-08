import sys

input = sys.stdin.readline

n = int(input())
dp = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    if i == 0: dp[i] = row
    else: 
        for j in range(len(row)):
            if j == 0:
                dp[i].append(row[j] + dp[i - 1][0])
            elif j == len(row) - 1:
                dp[i].append(row[j] + dp[i - 1][j - 1])
            else:
                dp[i].append(row[j] + max(dp[i - 1][j - 1], dp[i - 1][j]))
print(max(dp[-1]))