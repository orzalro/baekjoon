import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
e = int(input())

t = h * 3600 + m * 60 + s + e
h, m, s = t // 3600 % 24, t // 60 % 60, t % 60

print(h, m, s)