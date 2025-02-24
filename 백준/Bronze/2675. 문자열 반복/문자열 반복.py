import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    r, s = map(str, sys.stdin.readline().split())
    for j in s:
        print(j * int(r), end='')
    print()