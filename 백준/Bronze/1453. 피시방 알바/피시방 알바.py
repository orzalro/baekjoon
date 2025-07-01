import sys
input = sys.stdin.readline

n = int(input())
s = set(map(int, input().split()))
print(n - len(s))