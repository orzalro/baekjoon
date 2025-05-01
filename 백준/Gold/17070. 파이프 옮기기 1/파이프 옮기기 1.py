import sys

input = sys.stdin.readline

n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input().split())))

def calc():
    if house[-1][-1] == 1: return 0
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1
    for r in range(n):
        for c in range(2, n):
            if house[r][c] == 1: continue
            dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
            if r > 0:
                dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]
            if r > 0 and house[r - 1][c] == 0 and house[r][c - 1] == 0:
                dp[r][c][2] = sum(dp[r - 1][c - 1])
    return sum(dp[-1][-1])

print(calc())