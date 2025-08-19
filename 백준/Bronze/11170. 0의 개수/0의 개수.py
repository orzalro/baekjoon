import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(sum([str(num).count('0') for num in range(n, m + 1)]))