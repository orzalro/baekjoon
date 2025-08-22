import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]

maxq, minq = deque(), deque()
left = 0
max_len = 0
for right in range(n):
    while maxq and a[maxq[-1]] < a[right]:
        maxq.pop()
    maxq.append(right)

    while minq and a[minq[-1]] > a[right]:
        minq.pop()
    minq.append(right)

    while a[maxq[0]] - a[minq[0]] > 2:
        left += 1
        if maxq[0] < left:
            maxq.popleft()
        if minq[0] < left:
            minq.popleft()

    max_len = max(max_len, right - left + 1)

print(max_len)