import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

def calc(d):
    count = 1
    pre = x[0]

    for i in range(1, n):
        if x[i] - pre >= d:
            count += 1
            pre = x[i]

    return count

left = 1
right = x[-1] - x[0]

answer = 0

while left <= right:
    mid = (left + right) // 2

    if calc(mid) >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)