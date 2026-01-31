import sys
input = sys.stdin.readline

n = int(input())
l = [input().split() for _ in range(n)]
l.sort(key=(lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])))
[print(row[0]) for row in l]