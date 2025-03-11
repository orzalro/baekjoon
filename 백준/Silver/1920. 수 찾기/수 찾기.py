import sys

n = int(sys.stdin.readline().strip())
a = set(sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())
b = sys.stdin.readline().split()

for i in b:
    if i in a: print(1)
    else: print(0)