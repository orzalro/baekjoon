import sys
import heapq

input = sys.stdin.readline

n = int(input())
p_heap = []
n_heap = []

for i in range(n):
    x = int(input())

    if x == 0:
        if len(p_heap) > 0 and len(n_heap) > 0:
            x = heapq.heappop(p_heap) if p_heap[0] < n_heap[0] else -heapq.heappop(n_heap)
        elif len(p_heap) > 0:
            x = heapq.heappop(p_heap)
        elif len(n_heap) > 0:
            x = -heapq.heappop(n_heap)
        print(x)
    else:
        if x > 0:
            heapq.heappush(p_heap, x)
        else:
            heapq.heappush(n_heap, -x)