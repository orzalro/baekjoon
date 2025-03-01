import sys

def calc(i, j):
    if j == 0: return i
    return calc(j, i % j)

a, b = map(int, sys.stdin.readline().split())

gcd = calc(a, b)
lcm = int(a * b / gcd)
print(gcd)
print(lcm)