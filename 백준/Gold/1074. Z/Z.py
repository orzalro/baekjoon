import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

def calc(n, r, c):
    size = 2 ** n
    if size <= 2:
        return r * 2 + c

    if c < size // 2 and r < size // 2:
        return calc(n - 1, r, c)
    if c >= size // 2 and r < size // 2:
        return calc(n - 1, r, c - size // 2) + 4 ** (n - 1)
    if c < size // 2 and r >= size // 2:
        return calc(n - 1, r - size // 2, c) + 4 ** (n - 1) * 2
    if c >= size // 2 and r >= size // 2:
        return calc(n - 1, r - size // 2, c - size // 2) + 4 ** (n - 1) * 3

print(calc(n, r, c))