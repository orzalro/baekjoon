import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a, b = a - 1, b - 1
a_w, a_h = a // 4, a % 4
b_w, b_h = b // 4, b % 4
print(abs(a_w - b_w) + abs(a_h - b_h))