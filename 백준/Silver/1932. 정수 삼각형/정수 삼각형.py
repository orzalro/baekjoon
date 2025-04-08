import sys

input = sys.stdin.readline

n = int(input())
def gen(n):
    for _ in range(n):
        num = list(map(int, input().split()))
        yield num

dp = [[] for _ in range(n)]
for i, row in enumerate(gen(n)):
    if i == 0: dp[i] = row
    else: 
        for j, num in enumerate(row):
            if j == 0:
                dp[i].append(num + dp[i - 1][0])
            elif j == len(row) - 1:
                dp[i].append(num + dp[i - 1][j - 1])
            else:
                dp[i].append(num + max(dp[i - 1][j - 1], dp[i - 1][j]))
print(max(dp[-1]))