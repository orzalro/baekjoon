import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = sum(map(lambda x, y: 1 if x > y else -1 if y > x else 0, a, b))
print('A' if count > 0 else 'B' if count < 0 else 'D')