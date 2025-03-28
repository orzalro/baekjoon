import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
snake = {}

for i in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for i in range(m):
    u, v = map(int, input().split())
    snake[u] = v

def bfs():
    q = [1]
    next_q = []
    count = 0
    visited = set()

    while len(q) != 0:
        for cur in q:
            if cur == 100:
                next_q = []
                return count
            elif cur in ladder:
                visited.add(ladder[cur])
                q.append(ladder[cur])
            elif cur in snake:
                visited.add(snake[cur])
                q.append(snake[cur])
            else:
                for i in range(1, 7):
                    if cur + i <= 100 and cur + i not in visited:
                        visited.add(cur + i)
                        next_q.append(cur + i)
        q = next_q
        next_q = []
        count += 1

print(bfs())