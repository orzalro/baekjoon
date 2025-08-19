import sys
input = sys.stdin.readline

n = int(input())
x0, y0, e0 = map(int, input().split())
l = [[*map(int, input().split())] for _ in range(n)]

max_power = -1
for i in range(n):
    x, y, e = l[i]
    for j in range(n):
        if j == i: continue
        xt, yt, et = l[j]
        e += max(0, et - (abs(xt - x) + abs(yt - y)))
    max_power = max(max_power, e0 - (abs(x0 - x) + abs(y0 - y)) - e)

print(max_power if max_power > 0 else 'IMPOSSIBLE')