import sys

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())


s = 0
for i in l:
    if i % t != 0: s += 1
    s += i // t
print(s)
print(n // p, n % p)