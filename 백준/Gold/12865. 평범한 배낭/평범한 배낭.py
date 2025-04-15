import sys

input = sys.stdin.readline

n, k = map(int, input().split())

p = []
for i in range(n):
    w, v = map(int, input().split())
    p.append([w, v])

dp = {0: 0}
for w, v in p:
    temp = {}
    for dp_v, dp_w in dp.items():
        if dp.get(new_v:= dp_v + v, k + 1) > (new_w := dp_w + w):
            temp[new_v] = new_w
    dp.update(temp)

print(max(dp.keys()))