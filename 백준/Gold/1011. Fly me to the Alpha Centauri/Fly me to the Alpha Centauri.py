import sys
import bisect
input = sys.stdin.readline

n = 92682
arr = [i ** 2 // 4 for i in range(1, n + 1)]

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(bisect.bisect_left(arr, y - x))