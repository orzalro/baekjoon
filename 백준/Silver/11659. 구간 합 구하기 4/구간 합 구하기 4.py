import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix_num = {}
prefix_num[0] = 0
for i in range(1, n + 1):
    prefix_num[i] = prefix_num[i - 1] + num[i - 1]

for count in range(m):
    i, j = map(int, input().split())
    print(prefix_num[j] - prefix_num[i - 1])