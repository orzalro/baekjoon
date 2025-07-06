n, m, k = map(int, input().split())

if k < n + m - 1:
    print('NO')
else:
    print('YES')
    for i in range(1, n + 1):
        print(*range(i, m + i), sep = ' ')