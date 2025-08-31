import sys
input = sys.stdin.readline

n = int(input())
m = [i for i in range(n // 2 + 1, n + 1)]
s = [i for i in range(n // 2, 0, -1)]
if n % 2:
    [print(*row, sep = ' ', end=' ') for row in zip(m, s)]
    print(m[-1])
else:
    [print(*row, sep = ' ', end=' ') for row in zip(m, s)]