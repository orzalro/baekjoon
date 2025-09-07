import sys
input = sys.stdin.readline

t = int(input())
[print(sum(map(int, input().split()))) for _ in range(t)]