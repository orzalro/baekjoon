import sys
input = sys.stdin.readline

n = input()
n_l = set(input().split())
m = input()
print(*[int(i in n_l) for i in input().split()])