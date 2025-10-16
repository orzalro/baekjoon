import sys
input = sys.stdin.readline

n = int(input())
b = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    left, down = map(int, input().split())
    for i in range(left, left + 10):
        for j in range(down, down + 10):
            b[i][j] = 1
print(sum([sum(b[i]) for i in range(100)]))