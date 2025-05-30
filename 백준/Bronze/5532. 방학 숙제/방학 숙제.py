import sys
input = sys.stdin.readline

l, a, b, c, d = [int(input()) for _ in range(5)]
print(int(l - max(a / c, b / d)))