import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append([*map(int, input().split())])

l.sort()
s = l[0][0] + l[0][1]
for i in range(1, n):
    if s > l[i][0]:
        s += l[i][1]
    else:
        s = l[i][0] + l[i][1]
print(s)