import sys

input = sys.stdin.readline

n = int(input())

dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
for _ in range(n):
    num = list(map(int, input().split()))
    dp_max = [num[0] + max(dp_max[0:2]), num[1] + max(dp_max[0:3]), num[2] + max(dp_max[1:3])]
    dp_min = [num[0] + min(dp_min[0:2]), num[1] + min(dp_min[0:3]), num[2] + min(dp_min[1:3])]

print(max(dp_max), min(dp_min))