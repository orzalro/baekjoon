import sys
input = sys.stdin.readline

n = int(input())

min_x, min_y, max_x, max_y = map(int, input().split())
print(((max_x - min_x) + (max_y - min_y)) * 2)
for i in range(n - 1):
    a, b, c, d = map(int, input().split())
    min_x, min_y, max_x, max_y = min(min_x, a), min(min_y, b), max(max_x, c), max(max_y, d)
    print(((max_x - min_x) + (max_y - min_y)) * 2)