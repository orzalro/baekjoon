import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
l = [[0] * n for _ in range(n)]
answer = []

for i in range(m):
    string = list(map(int, input().split()))
    l[string[0] - 1][string[1] - 1] = 1
    l[string[1] - 1][string[0] - 1] = 1

for i in range(n):
    temp_list = [item[:] for item in l]
    q = deque()
    s = set()
    depth = 1
    total = {}
    temp = 0
    q.append(i)
    s.add(i)
    while len(q) != 0:
        a = q.popleft()
        for b in range(n):
            if temp_list[a][b] == 1 and b not in s:
                temp_list[a][b] = 0
                temp_list[b][a] = 0
                q.append(b)
                s.add(b)
                if depth in total: total[depth] += 1
                else: total[depth] = 1
        if temp == 0 and depth in total:
            temp = total[depth]
            depth += 1
        temp -= 1
    answer.append(sum([k * total[k] for k in total]))

print(answer.index(min(answer)) + 1)