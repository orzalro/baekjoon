import sys

m, n = map(int, sys.stdin.readline().split())

def calc(n):
    s = set(range(5, n + 1, 6)) | set(range(7, n + 1, 6))
    
    if n > 1: s.add(2)
    if n > 2: s.add(3)

    for i in range(5, int(n ** 0.5) + 1, 6):
        if i in s: s -= set(range(i * i, n + 1, 6 * i)) | set(range(i * (i + 2), n + 1, 6 * i))
        j = i + 2
        if j in s: s -= set(range(j * j, n + 1, 6 * j)) | set(range(j * (j + 4), n + 1, 6 * j))

    s -= set(range(m))
    return s

answer = list(calc(n))
answer.sort()
for i in answer:
    print(i)