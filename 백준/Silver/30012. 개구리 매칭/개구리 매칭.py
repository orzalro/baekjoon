import sys
input = sys.stdin.readline

s, n = map(int, input().split())
e_list = list(map(int, input().split()))
k, l = map(int, input().split())

minimum = float('inf')
for i, e in enumerate(e_list):
    if abs(s - e) > 2 * k:
        d = abs(s - e) - 2 * k
        if minimum > d * l:
            minimum, min_e = d * l, i + 1
    else:
        if minimum > 2 * k - abs(s - e):
            minimum, min_e = 2 * k - abs(s - e), i + 1
print(minimum, min_e)