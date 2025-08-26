import sys
input = sys.stdin.readline

day_d = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4}
t, n = map(int, input().split())
total_sleep_time = 0
for _ in range(n):
    d1, h1, d2, h2 = input().split()
    total_sleep_time += (day_d[d2] * 24 + int(h2)) - (day_d[d1] * 24 + int(h1))
t -= total_sleep_time

if t > 48:
    print(-1)
elif t >= 0:
    print(t)
else:
    print(0)