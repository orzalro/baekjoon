import sys
input = sys.stdin.readline

while True:
    try:
        n, p = map(int, input().split())
        if p > n // 2:
            if p % 2: l = [n - p, n - p + 1, p + 1]
            else: l = [n - p + 1, n - p + 2, p - 1]
        else:
            if p % 2: l = [p + 1, n - p, n - p + 1]
            else: l = [p - 1, n - p + 1, n - p + 2]
        print(' '.join(map(str, l)))
    except ValueError:
        break