import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
for i in range(1, n + 1):
    answer += sum([1 if sum(c) == s else 0 for c in combinations(numbers, i)])
print(answer)