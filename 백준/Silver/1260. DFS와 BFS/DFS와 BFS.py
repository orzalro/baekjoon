import sys

input = sys.stdin.readline

def dfs(v, l, s):
    s.add(v)
    answer = str(v)    
    for i in range(1, len(l)):
        if l[v][i] == 1 and i not in s:
            answer = ' '.join([answer, dfs(i, l, s)])
    return answer

def bfs(v, l):
    answer = str(v)
    s = set()
    s.add(v)
    next = [v]

    while len(next) != 0:
        v = next.pop(0)
        for i in range(1, len(l)):
            if l[v][i] == 1 and i not in s:
                answer = ' '.join([answer, str(i)])
                s.add(i)
                next.append(i)

    return answer

n, m, v = map(int, input().split())
line = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    line[a][b] = 1
    line[b][a] = 1

s = set()
print(dfs(v, line, s))
print(bfs(v, line))