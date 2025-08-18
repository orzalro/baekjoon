import sys
input = sys.stdin.readline

def ncr(n, r):
    result = 1
    for i in range(n, r, -1):
        result *= i
    for j in range(n - r, 1, -1):
        result = result // j
    return result
n, k = map(int, input().split())
print(ncr(n, k))