import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

def dfs(n, k):
    if n == k: return 0
    elif k == 1: return 1
    elif n < k:
        if k % 2 == 0:
            return min(k - n, dfs(n, k // 2) + 1)
        else:
            return 1 + min(dfs(n, k - 1), dfs(n, k + 1))
    else:
        return n - k

if n > k:
    print(n - k)
else:
    print(dfs(n, k))