import sys

input = sys.stdin.readline

d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
for i in range(4, 101):
    d[i] = sum(d[i - 3:i - 1])

for i in range(int(input())):
    print(d[int(input())])