import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[int(n) for n in input().strip()] for _ in range(n)]

visited = [[float('inf') for _ in range(m)] for _ in range(n)]
visited_b = [[float('inf') for _ in range(m)] for _ in range(n)]
visited[0][0] = 1

def bfs():
    q = [[1, 0, 0, 0]]
    new_q = []

    while q:
        while q:
            d, b, y, x = heapq.heappop(q)

            if b == 0:
                if y + 1 < n and graph[y + 1][x] == 0:
                    if d + 1 < visited[y + 1][x]:
                        heapq.heappush(new_q, [d + 1, b, y + 1, x])
                        visited[y + 1][x] = d + 1
                if y > 0 and graph[y - 1][x] == 0:
                    if d + 1 < visited[y - 1][x]:
                        heapq.heappush(new_q, [d + 1, b, y - 1, x])
                        visited[y - 1][x] = d + 1
                if x + 1 < m and graph[y][x + 1] == 0:
                    if d + 1 < visited[y][x + 1]:
                        heapq.heappush(new_q, [d + 1, b, y, x + 1])
                        visited[y][x + 1] = d + 1
                if x > 0 and graph[y][x - 1] == 0:
                    if d + 1 < visited[y][x - 1]:
                        heapq.heappush(new_q, [d + 1, b, y, x - 1])
                        visited[y][x - 1] = d + 1
                
                if y + 1 < n and graph[y + 1][x] == 1:
                    if d + 1 < visited[y + 1][x]:
                        heapq.heappush(new_q, [d + 1, b + 1, y + 1, x])
                        visited_b[y + 1][x] = d + 1
                if y > 0 and graph[y - 1][x] == 1:
                    if d + 1 < visited[y - 1][x]:
                        heapq.heappush(new_q, [d + 1, b + 1, y - 1, x])
                        visited_b[y - 1][x] = d + 1
                if x + 1 < m and graph[y][x + 1] == 1:
                    if d + 1 < visited[y][x + 1]:
                        heapq.heappush(new_q, [d + 1, b + 1, y, x + 1])
                        visited_b[y][x + 1] = d + 1
                if x > 0 and graph[y][x - 1] == 1:
                    if d + 1 < visited[y][x - 1]:
                        heapq.heappush(new_q, [d + 1, b + 1, y, x - 1])
                        visited_b[y][x - 1] = d + 1
            else:
                if y + 1 < n and graph[y + 1][x] == 0:
                    if d + 1 < visited[y + 1][x] and d + 1 < visited_b[y + 1][x]:
                        heapq.heappush(new_q, [d + 1, b, y + 1, x])
                        visited_b[y + 1][x] = d + 1
                if y > 0 and graph[y - 1][x] == 0:
                    if d + 1 < visited[y - 1][x] and d + 1 < visited_b[y - 1][x]:
                        heapq.heappush(new_q, [d + 1, b, y - 1, x])
                        visited_b[y - 1][x] = d + 1
                if x + 1 < m and graph[y][x + 1] == 0:
                    if d + 1 < visited[y][x + 1] and d + 1 < visited_b[y][x + 1]:
                        heapq.heappush(new_q, [d + 1, b, y, x + 1])
                        visited_b[y][x + 1] = d + 1
                if x > 0 and graph[y][x - 1] == 0:
                    if d + 1 < visited[y][x - 1] and d + 1 < visited_b[y][x - 1]:
                        heapq.heappush(new_q, [d + 1, b, y, x - 1])
                        visited_b[y][x - 1] = d + 1
        q = new_q
        new_q = []

bfs()
answer = min(visited[-1][-1], visited_b[-1][-1])
print(answer if answer != float('inf') else -1)