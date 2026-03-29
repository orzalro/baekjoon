import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

def calc():
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

lis = calc()
a.reverse()
lds = calc()
lds.reverse()

print(max(map(sum, zip(lis, lds))) - 1)