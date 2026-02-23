n = int(input())
dp1 = 1
dp2 = 2

for _ in range(1, n):
    dp1, dp2 = dp2 % 15746, (dp1 + dp2) % 15746

print(dp1)