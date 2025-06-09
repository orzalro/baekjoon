import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    answer = 0
    answer += abs(x1 - x2) + abs(y1 - y2) + z1 + z2
    print(answer)