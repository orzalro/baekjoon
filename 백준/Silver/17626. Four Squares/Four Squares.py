import sys

input = sys.stdin.readline

n = int(input().strip())

d = {}
d[1] = 1

def calc(n):
    if n in d: return d[n]
    min = 4
    for i in range(int(n ** 0.5), int((n // 4) ** 0.5), -1):
        remain = n - i ** 2
        if remain == 0:
            min = 1
            break
        elif remain in d:
            count = d[remain] + 1
        else:
            count = calc(remain) + 1
        if count < min:
            min = count
    d[n] = min
    return d[n]

print(calc(n))