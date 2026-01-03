import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

max_weight = 0
for i, weight in enumerate(ropes, 1):
    max_weight = max(max_weight, weight * i)
print(max_weight)