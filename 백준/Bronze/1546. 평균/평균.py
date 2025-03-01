import sys

n = int(sys.stdin.readline().strip())

l = list(map(int, sys.stdin.readline().split()))

print(sum(l) / max(l) * 100 / n)