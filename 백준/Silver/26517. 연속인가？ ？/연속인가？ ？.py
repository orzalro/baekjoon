import sys
input = sys.stdin.readline

k = int(input())
a, b, c, d = map(int, input().split())

f1 = a * k + b
f2 = c * k + d

if f1 == f2:
    print('Yes', f1)
else:
    print('No')