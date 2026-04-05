import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

count = [0] * 3

def divide(x1, y1, x2, y2):
    gap = (x2 - x1) // 3
    for y in range(y1, y2, gap):
        for x in range(x1, x2, gap):
            conquer(x, y, x + gap, y + gap)

def conquer(x1, y1, x2, y2):
    flag = paper[y1][x1]
    for y in range(y1, y2):
        for x in range(x1, x2):
            if paper[y][x] != flag:
                divide(x1, y1, x2, y2)
                return
    count[flag] += 1

conquer(0, 0, n, n)
print(count[-1])
print(count[0])
print(count[1])