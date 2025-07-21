import sys
input = sys.stdin.readline

n, k = map(int, input().split())
exp_list = list(map(int, input().split()))
total = 0

for i, exp in enumerate(sorted(exp_list)):
    total += min(i, k) * exp

print(total)