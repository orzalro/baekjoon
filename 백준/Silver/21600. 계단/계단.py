import sys
input = sys.stdin.readline

n = int(input())
h = [*map(int, input().split())]
max_length = 0
cur_length = 0
for i in range(n):
    if h[i] > cur_length:
        cur_length += 1
        max_length = max(max_length, cur_length)
    else:
        cur_length = h[i]
print(max_length)