import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
for i in sorted(l):
    print(i)