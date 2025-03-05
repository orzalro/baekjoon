import sys

n, k = map(int, (sys.stdin.readline().split()))

def calc(n, k):
    list = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                list[i][j] = 1
            else:
                list[i][j] = list[i - 1][j - 1] + list[i - 1][j]
    return list[n][k]

print(calc(n, k))