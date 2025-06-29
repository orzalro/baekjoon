import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def calc(n):
    if n in dp: return dp[n]
    if n % 2 == 0:
        a, b = n // 2, n // 2
    else:
        a, b = n // 2 + 1, n // 2
    total = a * b
    if a != 1:
        total += calc(a)
    if b != 1:
        total += calc(b)
    dp[n] = total
    return total

n = int(input())
dp = {}
dp[1] = 0
print(calc(n))