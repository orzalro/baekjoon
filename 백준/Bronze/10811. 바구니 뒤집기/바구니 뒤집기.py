import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    left = basket[:i - 1]
    middle = [*reversed(basket[i - 1:j])]
    right = basket[j:]
    basket = left + middle + right
print(*basket)