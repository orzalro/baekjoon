import sys
input = sys.stdin.readline

n, k = map(int, input().split())
exp_list = list(map(int, input().split()))

print(sum(min(i, k) * exp for i, exp in enumerate(sorted(exp_list))))