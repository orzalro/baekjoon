import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

pre = p[0]
top = p[0]
bottom = p[0]
max_height = 0
for i in range(1, n):
    if pre < p[i]:
        top = p[i]
        max_height = max(max_height, top - bottom)
    else:
        bottom = p[i]
    pre = p[i]

print(max_height)