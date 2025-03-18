import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
    heapq.heappush(heap, -num)