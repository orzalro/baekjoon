import sys

n = int(sys.stdin.readline().strip())
total = 0

l = list(map(int, sys.stdin.readline().split()))

for i in l:
    total += i / max(l) * 100

print(total / n)