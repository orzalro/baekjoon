import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.reverse()
lis = [0]

for i in range(n):
    if a[i] > lis[-1]:
        lis.append(a[i])
    elif a[i] < lis[-1]:
        lis[bisect_left(lis, a[i])] = a[i]

print(len(lis) - 1)