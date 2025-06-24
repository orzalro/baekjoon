import sys
input = sys.stdin.readline

n = int(input())
l = set(map(int, input().split()))

a = min(l)
if a != 1: a = 0
for i in range(1, n + 1):
    if (a + i) not in l:
        print(a + i)
        break