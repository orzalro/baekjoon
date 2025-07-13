import sys
input = sys.stdin.readline

q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    if y == 0:
        if x < 0: print(1)
        else: print(0)
    elif y > 0:
        if x < 0: print(2)
        else: print(1)
    else:
        if x < y: print(2)
        else: print(1)