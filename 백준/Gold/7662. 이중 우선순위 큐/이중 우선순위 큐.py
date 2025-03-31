import sys
import heapq

input = sys.stdin.readline

t = int(input())

for i in range(t):
    min_heap = []
    max_heap = []
    s = {}
    k = int(input())
    for j in range(k):
        command = input().strip().split()

        if command[0] == 'I':
            num = int(command[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in s: s[num] += 1
            else: s[num] = 1

        elif len(s) and command[0] == 'D':
            while True:
                if command[1] == '-1':
                    pop = heapq.heappop(min_heap)
                else:
                    pop = -heapq.heappop(max_heap)
                if pop in s:
                    s[pop] -= 1
                    if s[pop] == 0:
                        del s[pop]
                    break
            if len(s) == 0:
                min_heap = []
                max_heap = []
    
    q = list(s.keys())
    if len(s): print(max(q), min(q))
    else: print('EMPTY')