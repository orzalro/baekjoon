import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, k = map(int, input().split())

def calc(n, k):
    if n > k: return n - k
    elif n == k: return 0
    elif n < k:
        if n == 0:
            return 1 + calc(n + 1, k)
        elif k % 2 == 0:
            return min(k - n, calc(n, k // 2))
        else:
            return 1 + min(calc(n, k - 1), calc(n, k + 1))

print(calc(n, k))