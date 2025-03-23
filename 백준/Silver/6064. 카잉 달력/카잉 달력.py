import sys

input = sys.stdin.readline

t = int(input())
l = []

for i in range(t):
    m, n, x, y = map(int, input().split())
    l.append([m, n, x, y])

def Euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for m, n, x, y in l:
    i = 0
    max_num = m * n // Euclidean(m, n)
    while True:
        num = m * i + x
        if num % n == y or (y == n and num % n == 0):
            break
        if num > max_num:
            num = -1
            break
        i += 1
    print(num)