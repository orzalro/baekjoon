import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

answer = 0

while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    answer += a + b
    heapq.heappush(h, a + b)

print(answer)