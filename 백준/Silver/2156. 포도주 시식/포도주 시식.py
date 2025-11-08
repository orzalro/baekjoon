import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
dp0 = [0 for _ in range(n)]
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

dp1[0] = l[0]

for i in range(1, n):
    dp0[i] = max(dp0[i - 1], dp1[i - 1], dp2[i - 1])
    dp1[i] = dp0[i - 1] + l[i]
    dp2[i] = dp1[i - 1] + l[i]

print(max(dp0[-1], dp1[-1], dp2[-1]))