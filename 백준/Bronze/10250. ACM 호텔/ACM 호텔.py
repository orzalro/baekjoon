import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    h, w, n = map(int, (sys.stdin.readline().split()))
    f = n % h
    n = n // h
    if f == 0:
        f = h
        n += -1
    print(f'{f}{n + 1:02d}')