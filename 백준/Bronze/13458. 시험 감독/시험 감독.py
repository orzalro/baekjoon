import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]
b, c = map(int, input().split())

print(sum([max(0, i - b + c - 1) // c + 1 for i in a]))