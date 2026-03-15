import sys
input = sys.stdin.readline

def bfs(start_x, start_y, l):
    q = [[0, start_x, start_y]]
    new_q = []
    visited = [[float('inf') for _ in range(l)] for _ in range(l)]
    visited[start_x][start_y] = 0

    while q:
        for count, x, y in q:
            if x + 2 < l and y + 1 < l and count + 1 < visited[x + 2][y + 1]:
                new_q.append([count + 1, x + 2, y + 1])
                visited[x + 2][y + 1] = count + 1

            if x + 2 < l and y > 0 and count + 1 < visited[x + 2][y - 1]:
                new_q.append([count + 1, x + 2, y - 1])
                visited[x + 2][y - 1] = count + 1

            if x > 1 and y + 1 < l and count + 1 < visited[x - 2][y + 1]:
                new_q.append([count + 1, x - 2, y + 1])
                visited[x - 2][y + 1] = count + 1

            if x > 1 and y > 0 < l and count + 1 < visited[x - 2][y - 1]:
                new_q.append([count + 1, x - 2, y - 1])
                visited[x - 2][y - 1] = count + 1

            if x + 1 < l and y + 2 < l and count + 1 < visited[x + 1][y + 2]:
                new_q.append([count + 1, x + 1, y + 2])
                visited[x + 1][y + 2] = count + 1
                
            if x + 1 < l and y > 1 and count + 1 < visited[x + 1][y - 2]:
                new_q.append([count + 1, x + 1, y - 2])
                visited[x + 1][y - 2] = count + 1

            if x > 0 and y + 2 < l and count + 1 < visited[x - 1][y + 2]:
                new_q.append([count + 1, x - 1, y + 2])
                visited[x - 1][y + 2] = count + 1

            if x > 0 and y > 1 and count + 1 < visited[x - 1][y - 2]:
                new_q.append([count + 1, x - 1, y - 2])
                visited[x - 1][y - 2] = count + 1
        q = sorted(new_q, key=lambda x: x[0])
        new_q = []
    return visited


t = int(input())
i = [[int(input()), map(int, input().split()), map(int, input().split())] for _ in range(t)]
l = max(i, key=lambda x: x[0])[0]
visited = bfs(0, 0, l)

for l, (cur_x, cur_y), (dest_x, dest_y) in i:
    x_gap = abs(cur_x - dest_x)
    y_gap = abs(cur_y - dest_y)
    if x_gap > 1 and y_gap > 1:
        print(visited[x_gap][y_gap])
    else:
        print(bfs(cur_x, cur_y, l)[dest_x][dest_y])