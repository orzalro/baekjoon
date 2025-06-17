import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif pow(abs(r1 + r2), 2) < d or d < pow((r1 - r2), 2):
        print(0)
    elif d in [pow((r1 + r2), 2), pow(abs(r1 - r2), 2)]:
        print(1)
    elif pow(abs(r1 - r2), 2) < d or d < pow((r1 + r2), 2):
        print(2)