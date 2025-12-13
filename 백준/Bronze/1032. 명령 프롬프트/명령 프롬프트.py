import sys
input = sys.stdin.readline

n = int(input())
l = [input().strip() for _ in range(n)]
for i in range(len(l[0])):
    d = dict().fromkeys([row[i] for row in l])
    if len(d) == 1:
        print(list(d.keys())[0], end='')
    else:
        print('?', end='')