import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def calc(y, x):
    q = [(0, y, x)]
    new_q = []
    size = 2
    eating = 0
    time = 0

    graph[y][x] = 0

    visit_graph = [[True] * n for _ in range(n)]
    visit_graph[y][x] = 0

    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    while q:
        while q:
            t, y, x = heapq.heappop(q)
            if graph[y][x] < size and graph[y][x] != 0:
                time += t
                t = 0
                eating += 1
                if eating == size:
                    eating = 0
                    size += 1

                q = []
                new_q = []
                
                graph[y][x] = 0

                visit_graph = [[True] * n for _ in range(n)]
                visit_graph[y][x] = False
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and visit_graph[ny][nx]:
                    if graph[ny][nx] <= size:
                        visit_graph[ny][nx] = False
                        heapq.heappush(new_q, (t + 1, ny, nx))
        q = new_q
        new_q = []
    
    return time

for y in range(n):
    for x in range(n):
        if graph[y][x] == 9:
            print(calc(y, x))