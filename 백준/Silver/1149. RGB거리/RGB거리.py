import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, (input().split()))))
dp = [[0] * 3 for _ in range(n)]


def calc(i, c):
    if i == len(l) - 1: return l[i][c]
    if dp[i][c]: cost = dp[i][c]
    elif c == 0: cost = l[i][c] + min(calc(i + 1, 1), calc(i + 1, 2)); dp[i][c] = cost
    elif c == 1: cost = l[i][c] + min(calc(i + 1, 0), calc(i + 1, 2)); dp[i][c] = cost
    elif c == 2: cost = l[i][c] + min(calc(i + 1, 0), calc(i + 1, 1)); dp[i][c] = cost
    return cost

calc(0, 0)
calc(0, 1)
calc(0, 2)
print(min(dp[0]))